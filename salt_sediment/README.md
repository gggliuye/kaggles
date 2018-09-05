# TIMELINE
##  2018/07/29
#### first submission, 0.71, No.300
with model v2, 50 epochs
#### possible update:
 - more epochs, as the validation loss is still reducing             
 - take dropout to evide overfitting                                 
 - use new mean_iou                                                  
 - use one more channel of the np.cumsum() as input                  
 - changing the learning rate as training
 - test for the original Unet, to see if my model is good or not

## 2018/07/30
#### new change:
 - use mean_iou as monitor
 - change batch size to 64 -> 32 (resource not enough)
##### result 0.586  bad result
 - because of ouverfitting???	
	as for this problem, we only has two classes, and without complete situations, I think
	there won't be any problem of overfitting(in another word we want overfitting).

 - or I should not change the batch size??
	It is beacuse of the batch size. Model with larger batch size uses more resource in GPU,
	 which can acclerate the training process. But as the batch is large, the result tends 
	to converge in the local optimal result(training more likely to GD other than SGD).

 - the mean iou as monitor??
	From the result, the monitor value is getting better
	however the val_loss varies a lot from 0.7 to 0.1 between some epochs
	mayby is better to use default monitor

#### next training:
 - continue with the training in 7/29 for another 20 epochs
 - and test batch size 8 
 - ** deeplab choose: epoch = iteration * batch_size / num_image (make sense)

#### further thinking:
  I can change the learning rate, when it come to some local maximum -> take a larger learning rate 
