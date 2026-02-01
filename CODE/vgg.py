from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
#from tensorflow.keras import Model
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
import matplotlib.pylab as plt


train_dir=r"D:\FEBRUARY\FACE RECOGNITION\dataset\train"
test_dir=r"D:\FEBRUARY\FACE RECOGNITION\dataset\test"
train_augmentation = ImageDataGenerator(
                                    rescale=1./255,
                                    rotation_range=40,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    zoom_range = 0.2,
                                    horizontal_flip = True,)

train_gen = train_augmentation.flow_from_directory(train_dir,
                                                target_size=(128,128),
                                                batch_size=12,
                                                class_mode='categorical')

validation_augmentation=ImageDataGenerator(
                            rescale=1./255
                            )
validation_generator = validation_augmentation.flow_from_directory(test_dir,
                                                target_size=(128,128),
                                                batch_size=12,
                                                class_mode='categorical',
                                               )

conv_base=VGG16(input_shape=(128,128,3),include_top=False,weights='imagenet')

conv_base.summary()

for layer in conv_base.layers:
    layer.trainable=False

model=Sequential()
model.add(conv_base)
model.add(layers.Flatten())

model.add(layers.Dense(256,activation='relu'))
model.add(layers.Dense(7,activation='softmax'))

model.summary()

conv_base.trainable=True
set_trainable=False
for layer in conv_base.layers:
    if layer.name=='blocks_conv1':
        set_trainable=True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

history=model.fit(train_gen,
                  steps_per_epoch=8,
                  epochs=40,
                  verbose=1,
                  validation_data=validation_generator)

model.save(r"D:\FEBRUARY\FACE RECOGNITION\VGG16Model.h5")


plt.style.use("ggplot")
plt.figure()
plt.plot(history.history['accuracy'],'r',label='training accuracy',color='green')
plt.plot(history.history['val_accuracy'],label='validation accuracy')
plt.xlabel('# epochs')
plt.ylabel('loss')
plt.legend()
plt.savefig(r"D:\FEBRUARY\FACE RECOGNITION\\vgg.png")
plt.show()



vgg_acc=history.history['val_accuracy'][-1]
print(vgg_acc)

