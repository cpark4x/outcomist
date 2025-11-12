# AI Voiceover Generation Process

**Purpose**: Generate AI voiceover for demo videos and sync with sped-up video footage

## Problem Solved

When adding AI voiceover to high-frame-rate videos (120fps) and speeding them up, QuickTime displays incorrect duration because frame count doesn't match the new frame rate. Solution: Force output to 60fps during speed adjustment.

## Prerequisites

- Python 3.x with `openai` package installed
- ffmpeg installed
- OpenAI API key

## Files Created

- `generate_voiceover.py` - Main script for voiceover generation and video processing
- `voiceover.mp3` - Generated audio (temporary file)
- Output: `Demo-[ProjectName]-With-Voiceover.mp4`

## Script Structure

### 1. Voiceover Generation (OpenAI TTS)

```python
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.audio.speech.create(
    model="tts-1-hd",      # High quality model
    voice="echo",           # Clear, conversational male voice
    input=SCRIPT,
    speed=1.0               # Normal speed
)
response.stream_to_file("voiceover.mp3")
```

**Available voices**: alloy, echo, fable, onyx, nova, shimmer
**Speed range**: 0.25 to 4.0

### 2. Video Processing (Two-Step Approach)

**Critical Fix**: Force 60fps output to prevent duration miscalculation

#### Step 1: Speed up video
```bash
ffmpeg -i video_file \
  -filter:v "setpts={1/speed_multiplier}*PTS" \
  -r 60 \                    # CRITICAL: Force 60fps output
  -an \                       # Remove audio from source
  -c:v libx264 \
  -preset fast \
  -y temp_sped_up_video.mp4
```

#### Step 2: Add audio to sped-up video
```bash
ffmpeg -i temp_sped_up_video.mp4 \
  -i voiceover.mp3 \
  -c:v copy \                # Copy already encoded video
  -c:a aac \                 # Encode audio to AAC
  -b:a 192k \
  -map 0:v:0 \
  -map 1:a:0 \
  -shortest \                # Stop when audio ends
  -y output.mp4
```

## Why This Approach Works

### The Problem
- Original video: 120fps, 4:47 duration (34,440 frames)
- After speeding up 2x with setpts: Still has 34,440 frames but plays faster
- QuickTime calculation: 34,440 frames ÷ 120fps = 287 seconds (correct)
- But ffmpeg metadata showed 137 seconds
- **Result**: QuickTime confused, showed 7:04 instead of 2:17

### The Solution
- Force output to 60fps with `-r 60` flag
- After 2x speedup: 8,230 frames at 60fps
- QuickTime calculation: 8,230 frames ÷ 60fps = 137 seconds (2:17) ✓
- **Result**: Correct duration displayed

## Complete Workflow

### Initial Script Writing

1. **Write the script** (SCRIPT variable in Python file)
   - Keep it conversational and natural
   - Target length: Match desired video duration when sped up
   - Use `[PAUSE X]` markers for timing (will be processed by TTS)

2. **Set paths**
   ```python
   video_path = "~/Desktop/Demo-VideoName.mov"
   output_path = "~/Desktop/Demo-VideoName-With-Voiceover.mp4"
   ```

3. **Configure speed multiplier**
   ```python
   speed_multiplier = 2.0  # 2x faster (4:47 → 2:17)
   ```

4. **Run generation**
   ```bash
   cd project-demo-directory
   OPENAI_API_KEY='your-key' python3 generate_voiceover.py
   ```

5. **Verify output**
   ```bash
   ffprobe -v error -show_entries format=duration \
     -of default=noprint_wrappers=1:nokey=1 output.mp4
   ```

### Script Timing Synchronization (Optional but Recommended)

If narration doesn't match video timing, use frame analysis to synchronize:

6. **Extract key frames from video**
   ```bash
   # Extract frames at 0s, 5s, 15s, 30s, 50s, 75s, 100s, 125s
   ffmpeg -i output.mp4 \
     -vf "select='eq(n\,0)+eq(n\,300)+eq(n\,900)+eq(n\,1800)+eq(n\,3000)+eq(n\,4500)+eq(n\,6000)+eq(n\,7500)'" \
     -vsync 0 frame_%d.png
   ```

7. **Analyze frames** to understand what's shown at each timestamp

8. **Update SCRIPT** to match visual content:
   - Narrate what's actually on screen
   - Add longer `[PAUSE X]` markers during sections where viewers need to read text
   - Adjust pause durations to match visual transitions

9. **Regenerate video** with synchronized script

10. **Clean up**
    ```bash
    rm -f frame_*.png
    ```

## Usage for Future Projects

1. **Copy `generate_voiceover.py` to new project demo directory**

2. **Update the script**:
   - Modify `SCRIPT` variable with new narration
   - Update `video_path` to point to new video file
   - Update `output_path` for new output name
   - Adjust `speed_multiplier` if needed (2.0 = 2x faster)

3. **Choose appropriate voice**:
   - `echo` - Clear, conversational male (default choice)
   - `onyx` - Deep, authoritative male
   - `alloy` - Neutral, versatile
   - `nova` - Warm, engaging female
   - `shimmer` - Clear, professional female
   - `fable` - Expressive, dynamic

4. **Run the script** with your OpenAI API key

## Key Learnings

1. **Frame rate matters**: High fps videos (120fps) need explicit fps conversion
2. **Two-step process**: Separate speed adjustment from audio addition
3. **AAC encoding**: Better compatibility than copying MP3
4. **-shortest flag**: Ensures video stops when audio ends
5. **60fps output**: Good balance between quality and compatibility

## Troubleshooting

**Video shows wrong duration in QuickTime**:
- Ensure `-r 60` flag is present in Step 1
- Check frame count: `ffprobe -show_entries stream=nb_frames`
- Should be: (original_frames / speed_multiplier) / (original_fps / 60)

**Audio not playing**:
- Use AAC encoding (`-c:a aac`) instead of copying
- Add bitrate: `-b:a 192k`

**Video too fast/slow**:
- Adjust `speed_multiplier` in script
- Or adjust `speed` parameter in TTS generation (0.8-1.2 range)

## Script Template

```python
#!/usr/bin/env python3
"""
Generate AI voiceover for [Project Name] demo video.
"""

import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SCRIPT = """
[Your narration script here]
"""

# ... rest of generate_voiceover.py code ...

if __name__ == "__main__":
    video_path = str(Path.home() / "Desktop" / "Demo-[Project].mov")
    audio_path = "voiceover.mp3"
    output_path = str(Path.home() / "Desktop" / "Demo-[Project]-With-Voiceover.mp4")

    # Generate and combine (2x speedup)
    audio_file = generate_voiceover(audio_path)
    final_video = combine_audio_video(video_path, audio_file, output_path, speed_multiplier=2.0)
```

## Cost Considerations

- OpenAI TTS HD: ~$15 per million characters
- Example: 137-second narration ≈ 700 characters ≈ $0.01
- Very cost-effective for demo videos

## Future Enhancements

Possible improvements for future iterations:
- Support for multiple voiceover segments
- Background music mixing
- Subtitle generation
- Batch processing for multiple videos
- Voice cloning for consistent branding

---

**Created**: 2025-01-11
**Last Used**: Outcomist demo video generation
**Success Rate**: 100% after frame rate fix
