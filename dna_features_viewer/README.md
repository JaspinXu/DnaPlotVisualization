# Code organization

本文档引导您浏览DNA功能查看器代码。

- **GraphicFeature.py**实现了一个用于定义**GraphicFeature **的类，它是一个具有图形属性(颜色、线宽、字体系列……)的注释(开始、结束、串、标签)。

- **GraphicRecord/**实现了**GraphicRecord **类，它可以使用Matplotlib或Bokeh绘制一组** GraphicFeatures* *。为了保持文件大小可接受，许多方法都在单独的文件中实现(*bokeh_plots.py*、*matplotlib_plots.py*)，并通过类mixins添加到*GraphicRecord*中。

- **CircularGraphicRecord/**实现了** GraphicRecord* *类，它继承自** GraphicRecord* *，但使用名为“arrow-wedge”的自定义Matplotlib补丁循环绘制功能(定义在*ArrowWedge.py*文件中)。

- **compute_features_levels.py**实现了决定绘制不同特征(和注释)的级别的算法。

- **biotools.py**实现了与生物学相关的通用方法(反向补码、Biopython记录的注释等)。