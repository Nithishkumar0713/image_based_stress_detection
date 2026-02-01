from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,BatchNormalization
from tensorflow.keras.layers import Conv2D,MaxPooling2D
import os

num=7
r,c=48,48
b =32

t_train =r'dataset\train'
t_validation =r'dataset\test'

t1 = ImageDataGenerator(
					rescale=1./255,
					rotation_range=30,
					shear_range=0.3,
					zoom_range=0.3,
					width_shift_range=0.4,
					height_shift_range=0.4,
					horizontal_flip=True,
					fill_mode='nearest')

validation_data = ImageDataGenerator(rescale=1./255)

train_gen = t1.flow_from_directory(
					t_train,
					color_mode='grayscale',
					target_size=(r,c),
					batch_size= b,
					class_mode='categorical',
					shuffle=True)

validation_gen = validation_data.flow_from_directory(
							t_validation,
							color_mode='grayscale',
							target_size=(r,c),
							batch_size=b,
							class_mode='categorical',
							shuffle=True)


m = Sequential()



m.add(Conv2D(32,(3,3),padding='same',kernel_initializer='he_normal',input_shape=(r,c,1)))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(Conv2D(32,(3,3),padding='same',kernel_initializer='he_normal',input_shape=(r,c,1)))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(MaxPooling2D(pool_size=(2,2)))
m.add(Dropout(0.2))



m.add(Conv2D(64,(3,3),padding='same',kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(Conv2D(64,(3,3),padding='same',kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(MaxPooling2D(pool_size=(2,2)))
m.add(Dropout(0.2))



m.add(Conv2D(128,(3,3),padding='same',kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(Conv2D(128,(3,3),padding='same',kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(MaxPooling2D(pool_size=(2,2)))
m.add(Dropout(0.2))



m.add(Conv2D(256,(3,3),padding='same',kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(Conv2D(256,(3,3),padding='same',kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(MaxPooling2D(pool_size=(2,2)))
m.add(Dropout(0.2))



m.add(Flatten())
m.add(Dense(64,kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(Dropout(0.5))



m.add(Dense(64,kernel_initializer='he_normal'))
m.add(Activation('elu'))
m.add(BatchNormalization())
m.add(Dropout(0.5))



m.add(Dense(num,kernel_initializer='he_normal'))
m.add(Activation('softmax'))

print(m.summary())

from tensorflow.keras.optimizers import Adam
m.compile(loss='categorical_crossentropy',
              optimizer = Adam(lr=0.001),
              metrics=['accuracy'])

nb = 3006
e=500

h=m.fit_generator(
                train_gen,
                # steps_per_epoch=200,
                epochs=e,
                # callbacks=callbacks,
                validation_data=validation_gen,
				validation_steps=nb // b)

m.save(r"models\Vgg_Model.h5")

from matplotlib import pyplot as plt

plt.style.use("ggplot")
plt.figure()
plt.plot(h.h['accuracy'],'r',label='Validation accuracy',color='green')
# plt.plot(history.history['val_accuracy'],label='Validation accuracy')
plt.xlabel('# Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig(r"models\accuracy-2 .png")

plt.style.use("ggplot")
plt.figure()
plt.plot(h.h['loss'],'r',label='training loss',color='green')
# plt.plot(history.history['val_loss'],label='validation loss')
plt.xlabel('# Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig(r"models\loss-2.png")