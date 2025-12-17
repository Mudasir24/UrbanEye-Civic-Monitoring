from ultralytics import YOLO

model = YOLO("my_model.pt")

model.predict(
    source="test.mp4",
    save=True,
    conf=0.4,
    iou=0.5
)
