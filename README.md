# Personalized Image Captioning with Transformer Models

This project is a work in progress. The aim is to implement an image captioning system using transformer-based models like BERT or GPT. The system will automatically generate personalized captions for photos. The model will be trained to produce descriptive captions that capture the essence, context, and relevant details depicted in the photos, tailored to specific themes or topics.

## Objective

Implement an image captioning system using transformer-based models like BERT or GPT to automatically generate personalized captions for photos. Train the model to produce descriptive captions that capture the essence, context, and relevant details depicted in the photos, tailored to specific themes or topics.

## Learning Objectives

1. Understand the principles of image captioning and its applications in generating personalized content for social media platforms.
2. Gain familiarity with deep learning models for image captioning, including encoder-decoder architectures with attention mechanisms.
3. Learn techniques for preprocessing image and text data, including tokenization, numerical representation, and data augmentation.
4. Develop skills in model selection, training, and evaluation for image captioning tasks, with a focus on fine-tuning pre-trained models for specific domains.
5. Explore methods for deploying and integrating the captioning model into social media workflows for automatic caption generation.

## Use Case and Motivation

The primary use case for this project is to automate the process of generating captions for photos of my dogs on an [Instagram account](https://www.instagram.com/lol.a.chihuahua/). Each photo on this account features a unique caption, and this project aims to streamline that process.

The workflow consists of two main steps: first, a dog detection model identifies which of my dogs is in the photo; second, a caption generation model creates a relevant caption based on the photo's content and the dog's characteristics.

Once the caption is generated, the photo, along with the caption, can be automatically posted to Instagram. This automation simplifies the management of the Instagram account and ensures each post is accompanied by a personalized caption.

The motivation behind this project is to document and share moments with my two rescued Chihuahuas in an organized and engaging way. By utilizing AI techniques, I can efficiently generate creative and descriptive captions that enhance the storytelling aspect of each photo. The purpose of this project is to document the memories and experiences made with my dogs. 

## Project Development Notebooks

Below are the Jupyter notebooks created during the development of this project, listed in the order they were made:

1. [Training with Fast.ai](./notebooks/training-with-fast-ai.ipynb) - This notebook contains the steps and code for training a model using the Fast.ai library.

2. [Instruction Tuning GPT-2 on Alpaca Dataset](./notebooks/instruction-tunning-gpt2-alpaca.ipynb) - This notebook details the process of fine-tuning the GPT-2 model on the Alpaca dataset.

3. [Fine-Tuning GPT-2 on Custom Dataset](./notebooks/fine-tuning-gpt2-on-custom-dataset.ipynb) - This notebook demonstrates the steps to fine-tune the GPT-2 model on a custom dataset.

Stay tuned for more updates as the project progresses.

