from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")


def detect(image):
        input = processor(images=image, return_tensors="pt")
        output = model(**input)
        target_sizes = torch.tensor([image.size[::-1]])
        result = processor.post_process_object_detection(output, target_sizes=target_sizes, threshold=0.8)[0]
        return result, model