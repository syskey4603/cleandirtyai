from imageai.Classification.Custom import ClassificationModelTrainer

model_trainer = ClassificationModelTrainer()
model_trainer.setModelTypeAsResNet50()
model_trainer.setDataDirectory(r"C:/Users/vedan/OneDrive/Documents/Vedant/ai learn/hackathon proj/cleandirty")
model_trainer.trainModel(num_experiments=100, batch_size=32)