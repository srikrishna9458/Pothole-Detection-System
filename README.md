# Pothole Detection Project 🚗 🕳️

A real-time Computer Vision system designed to detect road hazards and potholes using **YOLOv8**. This project focuses on high-precision detection optimized for laptop hardware (RTX 3050), achieving inference speeds suitable for autonomous driving safety systems.

## 🎥 Project Demo
**[https://drive.google.com/file/d/1AURnKslc0QnDZA9YQV1fm4vq30-t4VrB/view?usp=sharing]**

*(Click the link above to watch the 4K detection demo)*

## 📊 Performance Metrics
The model was trained on a custom dataset of **1,900 annotated images** and optimized for real-time performance.

* **Precision:** **79%** (High reliability, minimizing false positives)
* **Inference Speed:** ~13ms per frame (**70+ FPS**)
* **Recall Strategy:** Inference pipeline tuned with a low confidence threshold (0.15) to maximize hazard detection in video feeds.

### Training Results
![Training Graphs](results.png)
*(Loss curves and performance metrics over 80 epochs)*

## 🛠️ Tech Stack
* **Model:** YOLOv8 (Medium Architecture)
* **Language:** Python 3.12
* **Libraries:** Ultralytics, OpenCV, PyTorch
* **Hardware:** Trained on NVIDIA RTX 3050 Laptop GPU

## 🚀 How to Run
1.  **Clone the repository**
2.  **Install dependencies:**
    ## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run inference: `python scripts/generate_final_video.py`
    
3.  **Run detection on your own video:**
    ```bash
    python detect.py
    ```

## 📂 Project Structure
* `detect.py`: The main inference script for video processing.
* `Pothole_Model.pt`: The trained YOLOv8 weights file.
* `results.png`: Training performance graphs.