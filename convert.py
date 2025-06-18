import os
import glob
import subprocess
from pathlib import Path

def convert_ogg_to_mp3_ffmpeg(input_folder=".", output_folder=None, bitrate="192k"):
    """
    Convert all .ogg files to .mp3 using FFmpeg directly
    
    Args:
        input_folder (str): Path to folder containing .ogg files
        output_folder (str): Path to save converted .mp3 files
        bitrate (str): Output bitrate for MP3 files
    """
    
    # Set output folder to input folder if not specified
    if output_folder is None:
        output_folder = input_folder
    
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Find all .ogg files in the input folder
    ogg_files = glob.glob(os.path.join(input_folder, "*.ogg"))
    
    if not ogg_files:
        print(f"No .ogg files found in '{input_folder}'")
        return
    
    print(f"Found {len(ogg_files)} .ogg files to convert")
    
    converted_count = 0
    failed_count = 0
    
    for ogg_file in ogg_files:
        try:
            # Get filename without extension
            filename = Path(ogg_file).stem
            output_file = os.path.join(output_folder, f"{filename}.mp3")
            
            print(f"Converting: {os.path.basename(ogg_file)} -> {os.path.basename(output_file)}")
            
            # FFmpeg command to convert OGG to MP3
            cmd = [
                'ffmpeg',
                '-i', ogg_file,
                '-b:a', bitrate,
                '-y',  # Overwrite output files without asking
                output_file
            ]
            
            # Run FFmpeg conversion
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                converted_count += 1
                print(f"✓ Successfully converted: {os.path.basename(ogg_file)}")
            else:
                print(f"✗ Error converting {os.path.basename(ogg_file)}")
                failed_count += 1
                
        except Exception as e:
            print(f"✗ Error converting {os.path.basename(ogg_file)}: {str(e)}")
            failed_count += 1
    
    print(f"\nConversion complete!")
    print(f"Successfully converted: {converted_count} files")
    if failed_count > 0:
        print(f"Failed conversions: {failed_count} files")

def check_ffmpeg():
    """Check if FFmpeg is available"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True)
        return True
    except FileNotFoundError:
        return False

def main():
    """
    Main function
    """
    
    # Check if FFmpeg is available
    if not check_ffmpeg():
        print("ERROR: FFmpeg not found!")
        print("Please install FFmpeg:")
        print("- Windows: Download from https://ffmpeg.org or use 'winget install ffmpeg'")
        print("- Mac: brew install ffmpeg")
        print("- Linux: sudo apt install ffmpeg")
        return
    
    # Configuration
    INPUT_FOLDER = r"C:/Users/VE/Downloads/Compressed/hindioldisgoldsongs"
    OUTPUT_FOLDER = None  # None = same as input folder or add patjh for output
    BITRATE = "192k"
    
    print("OGG to MP3 Batch Converter (FFmpeg)")
    print("=" * 35)
    
    convert_ogg_to_mp3_ffmpeg(
        input_folder=INPUT_FOLDER,
        output_folder=OUTPUT_FOLDER,
        bitrate=BITRATE
    )

if __name__ == "__main__":
    main()
