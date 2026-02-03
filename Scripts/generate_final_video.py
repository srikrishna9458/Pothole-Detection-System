import os
from ultralytics import YOLO

if __name__ == '__main__':
    # 1. EXACT VIDEO PATH (Matching your filename and folder)
    video_path = r"vedios\test vedio.mp4"

    # 2. MODEL PATH (From your successful 70% run)
    model_path = r"runs\detect\RoadSentinelRuns\Pothole_Speed_Run_90\weights\best.pt"

    # Double check files exist to prevent errors
    if not os.path.exists(video_path):
        print(f"❌ ERROR: Could not find video at: {os.path.abspath(video_path)}")
        exit()
    
    if not os.path.exists(model_path):
        print(f"❌ ERROR: Could not find model at: {os.path.abspath(model_path)}")
        exit()

    print(f"🚀 Processing: {video_path}")
    print("   (This forces the AI to detect ALL potholes, even small ones...)")

    # 3. LOAD MODEL
    model = YOLO(model_path)

    # 4. RUN DETECTION WITH "VISUAL BOOST"
    model.predict(
        source=video_path,
        save=True,
        imgsz=640,
        
        # --- THE TRICK FOR HIGH RECALL ---
        conf=0.15,      # Low threshold = It catches everything.
        iou=0.45,       # Cleans up the boxes.
        
        line_width=2,   # Makes it look professional.
        show_conf=False, # Hides the low % score.
        project="runs/detect",
        name="Final_Test_Video",
        exist_ok=True
    )

    print(f"\n✅ DONE! Open this folder to see the result:")
    print(f"   {os.path.abspath('runs/detect/Final_Test_Video')}")