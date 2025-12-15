# Names: Paul Hartman
# Lab: Lab5 (Basic Multimodal AI with Ollama)
# Date: 

## 2.1
1. Basic descriptions are a lot more summarized than detailed ones, mostly because they're shorter (one to two sentences). Detailed descriptions are sectioned.
2. The model focuses on colors the most out of all details. In the detailed descriptions, it covers pretty much everything you'd notice by looking at the image yourself, but it uses a lot of color-words to describe things and draws its higher-level analysis from the colors in the image. Ex: "The lighting is soft and natural, with a warm glow that enhances the colors and creates a pleasant atmosphere."

## 3.2
Adding guidelines does help; it has the greatest impact in situations where the classification is ambiguous and the guidelines offer criteria the model can use to distinguish its results.

## 4.1
1. The object count is innacurate (way too low when I ran it). Not necessary for this question but I found it interesting that the objects it "detected" included four color words, tying into my previous answer about how the model's vision capabilities utilize colors a lot for image understanding.
2. I went with a less confusing image:
![Picture of two and a half apples](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Pink_lady_and_cross_section.jpg/2560px-Pink_lady_and_cross_section.jpg)

The model got the object count right on this one, since it's less ambiguous (and each object is much more obvious). It did detect four "objects" for some reason: "Apple, apple slice, fruit, stem"