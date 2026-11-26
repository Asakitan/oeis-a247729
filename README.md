# 六项数组的等和禁配（A247729）

**证明署名：** Chain.Ren · 独立研究 · [完整证明](PROOF.md) · 版本日期：2026-11-26

[固定版本证明](https://github.com/Asakitan/oeis-a247729/blob/proof-v1.0.1/PROOF.md) · [GitHub Release 与公开时间](https://github.com/Asakitan/oeis-a247729/releases/tag/proof-v1.0.1) · [引用信息](CITATION.cff)

证明了 OEIS 所列十二个准多项式和一个普通生成函数。

[OEIS 原条目](https://oeis.org/A247729) · [完整证明](PROOF.md) · [MIT 许可证](LICENSE)

## 复核

Python 3.9+ 和 NumPy（可用 `python -m pip install -r requirements.txt` 安装）。 在仓库根目录运行：

~~~bash
python -B verify.py
~~~

有理顶点消元给出周期上界 12，整数状态递推核验 84 项，每个余数类七项。
