from matplotlib import rc_context
from A_linear_plot import CustomTranslator

rc_context({"path.sketch": (1.5, 300, 1)})  # scale, length, randomness


translator = CustomTranslator()
graphic_record = translator.translate_record("plasmid.gb")
cropped_record = graphic_record.crop((0, 1850))
ax, _ = cropped_record.plot(figure_width=2.5, with_ruler=False)
ax.figure.savefig("D_cartoon_plot.png", dpi=300, bbox_inches="tight")
