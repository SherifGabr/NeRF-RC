# NeRF Relighting & Compositing
NeRF-RC builds on the existing literature in 3D graphics and computer vision to develop a solution that integrates 3D mesh objects into a relightable scene generated by different NeRF (Neural Radiance Field) architectures. The solution allows for adjusting global lighting in a way that affects both the NeRF scene and the embedded 3D meshes. The integration of 3D meshes into NeRF scenes will result in more realistic and dynamic environments. The ability to adjust global lighting will further enhance the realism of the overall scene. The use of NeRF and NeRF Relighting has gained significant attention in both the computer vision and computer graphics communities in recent years due to its impressive results in reconstructing and relighting 3D scenes.

Completed under the supervision of: Prof. Dr. Janne Heikillä and Phong Nguyen

## Pipeline![pipeline-implementation](https://github.com/SherifGabr/NeRF-RC/assets/20493629/fff93102-6059-4fb6-b676-b8713d26e744)

1. NeRF-OSR to extract scene illumination.
2. NVDiffRec to extract object shape, BRDF, and illumination.
3. Combine novel lighting + novel viewpoint.
4. Render the result.

### 1. Scene illumination extraction

### 2. Object mesh extraction
![image](https://user-images.githubusercontent.com/20493629/216842943-edb20743-04ec-4c84-9991-63c31aaa75d4.png)

### 3. Scene-Object compositing
