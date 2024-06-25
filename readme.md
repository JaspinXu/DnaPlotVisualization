生命科学导论-DNA序列可视化器
--------------

使用python编译环境(如pycharm)打开文件后，为便于使用，请按下列步骤进行配置:

如果你已经安装了PIP，只需在终端中输入:

.. code:: bash

    pip install dna_features_viewer

DNA序列可视化器可以通过解压源代码到一个目录并使用这个命令来安装:

.. code:: bash

    python setup.py install

如果你打算使用bokeh功能，还需要安装bokeh和Pandas:

.. code:: bash

    pip install bokeh pandas

要解析GFF文件，需要安装``bcbio-gff``库:

.. code:: bash

    pip install bcbio-gff