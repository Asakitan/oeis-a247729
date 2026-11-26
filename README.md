# 六项数组的等和禁配（A247729）

证明了 OEIS 所列十二个准多项式和一个普通生成函数。

[OEIS 原条目](https://oeis.org/A247729) · [完整证明](PROOF.md) · [MIT 许可证](LICENSE)

## 复核

Python 3.9+ 和 NumPy（可用 `python -m pip install -r requirements.txt` 安装）。 在仓库根目录运行：

~~~bash
python -B verify.py
~~~

有理顶点消元给出周期上界 12，整数状态递推核验 84 项，每个余数类七项。

本工作给出可复核证明，不主张最早提出公式或全球首证。
