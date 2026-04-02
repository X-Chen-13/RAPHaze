# RAPHaze
The PyhHaze dataset can be downloaded here:https://drive.google.com/file/d/1hABPIoVCHDsxAO4BOVPfB0wO0dUQ-VJN/view?usp=drive_link
## 📁 Dataset Introduction
- **Number of datasets**：Ten thousand clear-fog paired remote sensing images
- **Spatial resolution**：480×640
- **Scene coverage**：Typical remote sensing scenes such as urban, mountain, water, vegetation and buildings
- **Fog concentration distribution**：The three levels of light fog, medium fog and thick fog are consistent with the fog distribution law of real remote sensing imaging
- **Dataset directory structure**
```markdown
PhyHaze/
├── train/         
│   ├── gt/         
│   └── hazy/      
└── test/          
    ├── gt/         
    └── hazy/     
```
## 📈 Experimental results
### Comparison of the generalization ability of the dataset on CUHK-CR2
We conduct a comprehensive quantitative evaluation of seven mainstream dehazing models on three remote sensing dehazing datasets (DHID, LHID, PhyHaze), covering both full-reference metrics (PSNR, SSIM, LPIPS, SAM) and no-reference metrics (BRISQUE).

| Method          | Dataset | PSNR↑    | SSIM↑   | LPIPS↓  | SAM↓    | BRISQUE↓ |
|-----------------|---------|----------|---------|---------|---------|----------|
| DCI-Net         | DHID    | 11.316   | 0.420   | **0.412** | 0.092   | 0.270    |
|                 | LHID    | **11.983** | **0.451** | 0.414   | **0.068** | **0.210** |
|                 | RAPHaze | 10.984   | 0.410   | 0.419   | 0.085   | 0.231    |
| FocalNet        | DHID    | 10.517   | 0.419   | 0.433   | 0.084   | 0.293    |
|                 | LHID    | 10.399   | 0.391   | 0.438   | 0.108   | 0.231    |
|                 | RAPHaze | **13.933** | **0.496** | **0.400** | **0.044** | **0.166** |
| OKNet           | DHID    | 10.248   | 0.398   | 0.428   | 0.091   | 0.281    |
|                 | LHID    | 10.424   | 0.394   | 0.437   | 0.102   | 0.210    |
|                 | RAPHaze | **10.720** | **0.433** | **0.409** | **0.077** | **0.204** |
| PSMB-Net        | DHID    | 10.422   | 0.409   | 0.440   | **0.073** | **0.192** |
|                 | LHID    | **12.615** | **0.479** | 0.409   | 0.088   | 0.215    |
|                 | RAPHaze | 11.643   | 0.449   | 0.402   | 0.090   | 0.213    |
| ACA-CRNet       | DHID    | 9.898    | 0.336   | 0.377   | 0.106   | 0.720    |
|                 | LHID    | 10.401   | 0.328   | 0.390   | 0.085   | 0.509    |
|                 | RAPHaze | **10.668** | **0.369** | **0.351** | **0.066** | **0.506** |
| DGFDNet         | DHID    | 10.507   | 0.406   | 0.420   | 0.090   | 0.269    |
|                 | LHID    | 11.400   | 0.442   | 0.417   | 0.075   | **0.191** |
|                 | RAPHaze | **14.005** | **0.496** | **0.391** | **0.044** | **0.158** |
| DehazeSNN       | DHID    | 10.223   | 0.417   | 0.440   | 0.089   | 0.205    |
|                 | LHID    | **12.627** | **0.480** | 0.407   | **0.069** | **0.187** |
|                 | RAPHaze | 12.024   | 0.483   | 0.401   | 0.079   | 0.194    |
### Visual comparison of dehazing effect
![去雾效果对比图](./assets/Qualitative_comparisons3.png)
### Quantitative comparison of geostatistical metrics
| Metric | RAPH. | DHID | LHID | CUHK | RRSHID | T-cloud. | RICE |
|--------|-------|------|------|------|--------|----------|------|
| Moran's I | 0.849 | 0.829 | 0.729 | 0.856 | 0.887 | 0.862 | 0.813 |
| Spatial Range | 26.15 | 22.51 | 22.91 | 26.75 | 28.13 | 26.57 | 25.86 |
