import cv2
from cv2 import rectangle, imread, imwrite

def save_bbox(filename, results):
    img = imread(filename)
    label = results[0]['name']
    labelSize=cv2.getTextSize(label,cv2.FONT_HERSHEY_COMPLEX,0.5,2)
    for result in results:
        if result['type'] == 'bug':
            color = (0, 0, 255)
        else:
            color = (255, 0, 0)
        
        rectangle(img, result['bbox'][0], result['bbox'][1], color, 2)
        
        label = result['name']
        labelSize = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)

        _x1, _y1 = result['bbox'][0]
        _x2 = _x1 + labelSize[0][0] + 3
        _y2 = _y1 + int(labelSize[0][1])
        cv2.rectangle(img,(_x1,_y1),(_x2,_y2), color, cv2.FILLED)
        cv2.putText(img,label,(_x1 + 2 ,_y2 -2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255 , 255 , 255),1)

    imwrite(filename, img)
