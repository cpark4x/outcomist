#!/usr/bin/env python3
"""
Generate AI voiceover for Outcomist demo video using OpenAI TTS.
"""

import os
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Script synchronized with video timing based on frame analysis
SCRIPT = """
Most people don't know what they actually want. They ask AI for solutions... but is that even the right problem?

[PAUSE 3]

That's why I built Outcomist. AI that drives outcomes, not activities.

[PAUSE 3]

I built this in three to four days using Amplifier. Two interfaces. Same engine.

[PAUSE 2]

Let me show you how it works.

[PAUSE 4]

The CLI runs through Claude Code. I'm typing slash explore... asking about redesigning my office.

[PAUSE 8]

Watch what happens. Instead of jumping to solutions, it's asking why.

[PAUSE 5]

See these questions? What's driving the redesign? What's your current situation? What are you looking for?

[PAUSE 6]

Most AI would immediately suggest furniture or layouts. But Outcomist wants to understand the real problem first.

[PAUSE 8]

I tell it my office is cluttered and disorganized. Not inspiring. Now watch this response.

[PAUSE 8]

It's breaking down what I said. Quick analysis. You've got a functional setup but it's not working. The clutter and uninspiring feel suggest something deeper.

[PAUSE 6]

Then it asks where the clutter is coming from. Papers piling up? Random items without a home? What would inspiring look like to me?

[PAUSE 6]

It's not giving me answers. It's helping me think more clearly about the problem.

[PAUSE 5]

That's what ChatGPT would miss. The real question underneath.

[PAUSE 3]

I built this CLI in two days. Two days from idea to working tool.

[PAUSE 4]

Now the web version. Same engine, visual interface.

[PAUSE 8]

I'm asking about timing a side hustle. Watch this.

[PAUSE 6]

It immediately asks about my current constraints. What does a typical week look like? Between work, family commitments... where would I find time?

[PAUSE 8]

I tell it I can spend a few hours each night with my son. Now look at this response.

[PAUSE 6]

It recognizes two motivations. Extra income and creating a learning opportunity with Mason. That's actually a great combination.

[PAUSE 6]

See? It remembers my son's name. It knows what matters to me. This isn't generic advice. This is specific to my life.

[PAUSE 4]

That's the power of memory and context.

[PAUSE 3]

I built the CLI in two days. The web app in one to two days.

[PAUSE 3]

That's the power of Amplifier. A development approach that combines AI with proven patterns.

[PAUSE 3]

I orchestrated AI to handle implementation while I focused on the experience I wanted to create.

[PAUSE 3]

The result? Something that would have taken weeks took days. And it works. You just saw it.

[PAUSE 3]

This is what's possible when you combine clear thinking with the right tools.

[PAUSE 2]

Link to Amplifier in the description. Thanks for watching.
"""

def generate_voiceover(output_file: str = "voiceover.mp3"):
    """Generate voiceover audio using OpenAI TTS."""
    print(f"Generating voiceover audio...")

    response = client.audio.speech.create(
        model="tts-1-hd",  # Higher quality model
        voice="echo",      # Clear, conversational male voice (options: alloy, echo, fable, onyx, nova, shimmer)
        input=SCRIPT,
        speed=1.0          # Normal speed for extended script (can adjust 0.25 to 4.0)
    )

    # Save audio file
    response.stream_to_file(output_file)
    print(f"✓ Voiceover saved to: {output_file}")

    return output_file

def combine_audio_video(video_file: str, audio_file: str, output_file: str = "demo_with_voiceover.mp4", speed_multiplier: float = 1.0):
    """Combine voiceover audio with video using ffmpeg, optionally speeding up the video."""
    import subprocess

    print(f"\nCombining audio with video...")
    if speed_multiplier != 1.0:
        print(f"Speeding up video by {speed_multiplier}x...")

    if speed_multiplier == 1.0:
        # Use ffmpeg to add audio to video without speed change
        cmd = [
            "ffmpeg",
            "-i", video_file,        # Input video
            "-i", audio_file,        # Input audio
            "-c:v", "copy",          # Copy video codec (no re-encoding)
            "-c:a", "aac",           # Audio codec
            "-map", "0:v:0",         # Map video from first input
            "-map", "1:a:0",         # Map audio from second input
            "-shortest",             # End when shortest stream ends
            "-y",                    # Overwrite output file
            output_file
        ]
    else:
        # Two-step process: 1) Speed up video, 2) Add audio
        temp_video = "temp_sped_up_video.mp4"

        # Step 1: Speed up the video using setpts filter and re-encode
        print(f"  Step 1: Speeding up video to {speed_multiplier}x...")
        speed_cmd = [
            "ffmpeg",
            "-i", video_file,
            "-filter:v", f"setpts={1/speed_multiplier}*PTS",
            "-r", "60",  # Force output to 60fps for compatibility
            "-an",  # Remove audio from source
            "-c:v", "libx264",
            "-preset", "fast",
            "-y",
            temp_video
        ]

        result = subprocess.run(speed_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"✗ Error speeding up video:")
            print(result.stderr)
            return None

        print(f"  Step 2: Adding audio to sped-up video...")
        # Step 2: Add audio to the sped-up video
        cmd = [
            "ffmpeg",
            "-i", temp_video,
            "-i", audio_file,
            "-c:v", "copy",  # Copy already encoded video
            "-c:a", "aac",
            "-b:a", "192k",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            "-y",
            output_file
        ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✓ Video with voiceover saved to: {output_file}")
        # Clean up temp file if it exists
        if speed_multiplier != 1.0:
            import os
            try:
                os.remove(temp_video)
            except:
                pass
        return output_file
    else:
        print(f"✗ Error combining audio and video:")
        print(result.stderr)
        return None

if __name__ == "__main__":
    # Set paths
    video_path = str(Path.home() / "Desktop" / "Demo-Outcomist v2.mov")
    audio_path = "voiceover.mp3"
    output_path = str(Path.home() / "Desktop" / "Demo-Outcomist-v2-With-Voiceover.mp4")

    print("🎙️  Outcomist Demo Voiceover Generator\n")
    print(f"Video: {video_path}")

    # Check if video exists
    if not Path(video_path).exists():
        print(f"✗ Error: Video file not found: {video_path}")
        exit(1)

    # Check for OpenAI API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("✗ Error: OPENAI_API_KEY environment variable not set")
        print("   Set it with: export OPENAI_API_KEY='your-openai-api-key'")
        exit(1)

    try:
        # Step 1: Generate voiceover
        audio_file = generate_voiceover(audio_path)

        # Step 2: Combine with video (speed up video by 2x to make 4:47 → ~2:24)
        final_video = combine_audio_video(video_path, audio_file, output_path, speed_multiplier=2.0)

        if final_video:
            print(f"\n✅ Done! Your video with voiceover is ready:")
            print(f"   {final_video}")
            print(f"\n💡 Tip: If timing is off, you can:")
            print(f"   1. Adjust 'speed' parameter in generate_voiceover() (0.8 = slower, 1.2 = faster)")
            print(f"   2. Edit timing manually in iMovie or DaVinci Resolve")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
