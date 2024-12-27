# PyNDI
PyNDI (NTU Damage Index calculator) provides a simulator-based calculator for damage index calculation.
## Overview
The damage index calculated in this program is basically based on the FEDI (Fire and Explosion Damage Index).
Firstly, hazadous chemicals will be defined in advance. 
Secondly, the program will search the and determine which unit may provide the most huge FEDI and let it represent the whole process.
By these two steps, the operation iteration can be reduced.
Finally, this progream connect with Aspen Plus for damage index evaluation.

## Required Package
```bash
pip install -r requirements.txt
```
or intall through 
```bash
pip install PyNDI
```

## Acknowlege
The primary developer is Pei-Jhen Wu with support from the following contributors.
* Bor-Yih Yu (National Taiwan University)
* Hsuan-Han Chiu (Purdue Universtiy)

## References
1. AIChE, Dow's Fire & Explosion Index Hazard Classification Guide. 1994.
2. Gupta, J.P., et al., Calculation of Fire and Explosion Index (F&EI) value for the Dow Guide taking credit for the loss control measures. Journal of Loss Prevention in the Process Industries, 2003. 16(4): p. 235-241.
3. Heikkilä, A.-M., Inherent safety in process plant design: an index-based approach. 1999: VTT Technical Research Centre of Finland.
4. Teh, S.Y., et al., A hybrid multi-objective optimization framework for preliminary process design based on health, safety and environmental impact. Processes, 2019. 7(4): p. 200.
5. Sharma, S., et al., Process design for economic, environmental and safety objectives with an application to the cumene process. Multi‐Objective Optimization in Chemical Engineering: Developments and Applications, 2013: p. 449-477.


## Citing
``` sourceCode
@article{Safety Considerations in CO2 Conversion: Production of Glycerol Carbonate via an Indirect Pathway,
author = {PJ. Wu, HH. Chiu, BY. Yu},
journal = {Journal of Industrial and Engineering Chemistry},
pages = {},
title = {},
volume = {},
year = {},
doi = {}
}
```