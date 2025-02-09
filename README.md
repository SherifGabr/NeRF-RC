# NeRF Relighting & Compositing
NeRF-RC builds on the existing literature in 3D graphics and computer vision to develop a solution that integrates 3D mesh objects into a relightable scene generated by different NeRF (Neural Radiance Field) architectures. The solution allows for adjusting global lighting in a way that affects both the NeRF scene and the embedded 3D meshes. Integrating 3D meshes into NeRF scenes will create more realistic and dynamic environments. The ability to adjust global lighting will further enhance the realism of the overall scene. NeRF and NeRF Relighting have gained significant attention in both the computer vision and computer graphics communities in recent years due to their impressive results in reconstructing and relighting 3D scenes.

Completed under the supervision of Prof. Dr. Janne Heikkilä and Phong Nguyen
### Thesis
http://jultika.oulu.fi/Record/nbnfioulu-202306152524

## Pipeline![pipeline-implementation](https://github.com/SherifGabr/NeRF-RC/assets/20493629/fff93102-6059-4fb6-b676-b8713d26e744)

1. NeRF-OSR to extract scene geometry, texture, and illumination.
2. NVDiffRec to extract object shape, BRDF, and illumination.
3. Combine novel lighting + novel viewpoint.
4. Render the result.

### 1. Scene extraction
![BistroResults](https://github.com/SherifGabr/NeRF-RC/assets/20493629/990b16b5-350b-42b2-8a5c-6c8dcaba80b6)

### 2. Object mesh extraction
![EgyptianChair](https://github.com/SherifGabr/NeRF-RC/assets/20493629/eeeb45bb-3da9-42c0-a715-79a5a5c099ae)

### 3. Scene-Object compositing

### Additional
## NeRF Multi-Layer Perceptron (MLP)
![NeRF-MLP](https://github.com/SherifGabr/NeRF-RC/assets/20493629/473f459c-221c-4316-bbae-30467240d639)
