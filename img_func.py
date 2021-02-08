import cv2

def bounding_box(img, results):
    
    for result in results:
        if result['type'] == 'bug':
            cv2.rectangle(img, (0, 0), (100, 100), (255,0,0), 2)
        else:
            cv2.rectangle(img, (0, 0), (100, 100), (0,0,255), 2)
    
    return img
