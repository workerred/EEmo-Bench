<div align="center">

 <div>
<a href="https://github.com/workerred/EEmo-Bench"><img src="https://img.shields.io/github/stars/workerred/EEmo-Bench"/></a>
    <a href="https://arxiv.org/abs/2504.16405"><img src="https://img.shields.io/badge/Arxiv-2504.16405-yellow"/></a>
    <a href="https://huggingface.co/datasets/Workerred/EEmo-Bench_single"><img src="https://img.shields.io/badge/Data-EEmoBench_single-green"></a>
    <a href="https://huggingface.co/datasets/Workerred/EEmo-Bench_pair"><img src="https://img.shields.io/badge/Data-EEmoBench_pair-blue"></a>
</div>

<h1>EEmo-Bench: A Benchmark for Multi-modal Large Language Models on Image Evoked Emotion Assessment</h1>

_How MLLMs Perform on Image Evoked Emotion Understanding?_

<div>
    <a href="https://scholar.google.com.hk/citations?hl=zh-CN&user=6KCeFTQAAAAJ&view_op=list_works&gmla=AH8HC4zpp4nUK5A3YmkhcwdHF2O5NwoCsCInYb0SW2ZHWxl-tUMaE_8OISiYvwIAfFSyg033cF7FLxHchO-sedO9qI_fHD0QlzjsiUCAvSc" target="_blank">Lancheng Gao</a><sup>1</sup>,
    <a href="https://scholar.google.com/citations?user=JYqad5sAAAAJ&hl=zh-CN" target="_blank">Ziheng Jia</a><sup>1</sup>,
    <a href="https://orcid.org/0009-0001-6429-5763" target="_blank">Yunhao Zeng</a><sup>1</sup>,
    <a href="https://scholar.google.com/citations?hl=zh-CN&user=nDlEBJ8AAAAJ" target="_blank">Wei Sun</a><sup>1</sup>,
</div>

<div>
    <a href="https://github.com/mingZhang614" target="_blank">Yiming Zhang</a><sup>1</sup>,
    <a href="https://scholar.google.com/citations?hl=en&user=vbR9_cgAAAAJ&view_op=list_works&sortby=pubdate" target="_blank">Wei Zhou</a><sup>2</sup>,
    <a href="https://ee.sjtu.edu.cn/en/FacultyDetail.aspx?id=24&infoid=153&flag=153" target="_blank">Guangtao Zhai</a><sup>1</sup>,
    <a href="https://minxiongkuo.github.io/" target="_blank">Xiongkuo Min</a><sup>1</sup><sup>#</sup>
</div>
  <div>
        <sup>1</sup>Shanghai Jiaotong University,  <sup>2</sup>Cardiff University
    </div>   
<div>
    <sup># </sup>Corresponding author. 
</div>

<div>
    <a href="https://arxiv.org/abs/2504.16405"><strong>Paper</strong></a> |
    <a href="https://github.com/workerred/EEmo-Bench"><strong>Github</strong></a> |
    <a href="https://huggingface.co/datasets/Workerred/EEmo-Bench_single"><strong>Single Image Data</strong></a>   |
    <a href="ttps://huggingface.co/datasets/Workerred/EEmo-Bench_pair"><strong>Image Pair Data</strong></a>  
</div>

<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="Diagram.png">
</div>

<div align="left">

we introduce **EEmo-Bench**, a novel benchmark dedicated to the analysis of the <u>e</u>voked <u>emo</u>tions in images across diverse content categories. Our core contributions include:
  1. Regarding the diversity of the evoked emotions, we adopt an emotion ranking strategy and employ the Valence-Arousal-Dominance (VAD) as emotional attributes for emotional assessment. In line with this methodology, 1,960 images are collected and manually annotated.
  2. We design four tasks to evaluate MLLMs' ability to capture the evoked emotions by single images and their associated attributes: **Perception**, **Ranking**, **Description**, and **Assessment**. Additionally, image-pairwise analysis is introduced to investigate the model's proficiency in performing joint and comparative analysis.
  
  In total, we collect 6,773 question-answer pairs and perform a thorough assessment on 19 commonly-used MLLMs.
  The results indicate that while some proprietary and large-scale open-source MLLMs achieve promising overall performance, the analytical capabilities in certain evaluation dimensions remain suboptimal.
  Our **EEmo-Bench** paves the path for further research aimed at enhancing the comprehensive perceiving and understanding capabilities of MLLMs concerning image-evoked emotions, which is crucial for machine-centric emotion perception and understanding.

## Release
- [2025/7/7] 🔥 Release official Results of 19 commonly-used MLLMs on EEmo-Bench, click on [leaderboards](https://github.com/workerred/EEmo-Bench/tree/main/leaderboards) to view details
- [2025/7/6] 🔥 Release the sample script for testing on EEmo-Bench.
- [2025/7/5] 🔥 Release [single-image](https://huggingface.co/datasets/Workerred/EEmo-Bench_single) and [image-pair](https://huggingface.co/datasets/Workerred/EEmo-Bench_pair) evoked emotion understanding question-answer datasets.
- [2025/7/4] 🔥 Our work ["EEmo-Bench: A Benchmark for Multi-modal Large Language Models on Image Evoked Emotion Assessment"](https://arxiv.org/abs/2504.16405) is accepted by ACMMM 2025.

## EEmo-Bench Construction
For each image in EEmo-Bench, a content category and two types of emotional attributes are attached: 

1. **Content category.**
    - **Six category**: Animal, Human, Stationary object, Daily life scene, Natural landscape, and Abstract/Cartoon image.
2. **Evoked emotions ranked by intensity.** 
   - **7 basic emotions**: Joy, Anger, Disgust, Sadness, Surprise, Fear, and Neutral.
   - We rank the **top three** evoked emotions from strongest to weakest (*e.g.*, [Joy, Neutral, Surprise])
3. **VAD scores** (Self-Assessment Manikin 9-point scale).
    - **Valence**, which reflects the overall positive or negative emotion elicited by images, indicating the emotional tone of the viewer’s response.
    - **Arousal**, which represents the intensity of theevoked emotion, rating from intense to calm.
    - **Dominance**, which measures the degree of influence over emotions and determines how emotions are experienced in terms of one’s sense of agency and authority in a particular emotional context, ranging from powerful to helpless.

Based on the constructed dataset and emotional attributes, we propose **EEmo-Bench** to omprehensively evaluate the evoked emotion understanding abilities of multiple MLLMs from four tasks, including **Perception**, **Ranking**, **Description**, and **Assessment**. The brief introduction subcategories are organized as follows:

1. **Perception.** The perception task concentrates on evaluating the evoked emotion perception abilities of MLLMs, focusing on their accuracy in question answering related to emotion category and emotional attributes.
   - **Question types**: Yes-or-No questions, What/How questions.
   - **Carrier**: Single-image, Image-pair.
   - **Perceptual_dimension**: Emotion perception, Valence perception, Arousal perception, Dominance perception.
   - **Question_concern**: Attributes perception, Reasoning perception, Similarity perception, Differences comparison.

2. **Ranking.** During each MLLM evaluation, the seven candidate emotions are provided as options, and we instruct the MLLMs to choose and rank no more than three predominant evoked emotions according to their intensity.

3. **Description.** We also assess the descriptive abilities of MLLMs.
   - **Carrier**: Single-image, Image-pair. 
   - **Describing dimension**: Detailed description, Reasoning description, Direct-Indirect, Conflicts description, Detailed comparison, Valence comparison, Arousal comparison, Dominance comparison, and other.

4. **Assessment.** In the final task, we benchmark the ability of MLLMs to quantify the VAD scores. 
   
<div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="Example.png">
  </div>

## Glance at Q-Bench-Video Performance

<div align="left">
<div style="width: 100%; text-align: center; margin:auto;">
  <img style="width:40%" src="overall.png">
  <img style="width:54%" src="description.png">
</div>
<div style="width: 100%; text-align: center; margin:auto;">
  <img style="width:40%" src="perception.png">
  <img style="width:46%" src="Tab4.png">
</div>
   