# SJQU-Health-Report
建桥i健康自动打卡

## 使用方法
1. 请 [Fork](https://github.com/missuo/bojj1/SJQU-Health-Report/fork) 本仓库。

2. 请在点击 `设置` - `Secrets`，添加 `USERNAME` 和 `PASSWORD`。

3. 点击 `Actions`，开启 `Github Actions` 即可。

4. 在 `GenchAPI 0.0.6` 中支持了不在校/在校的选择。修改 `main.py` 第三行。
```python
# 默认不传参数代表在校
GenchAPI.sign(os.environ.get('username') , os.environ.get('password'))
# 传参数0代表不在校
GenchAPI.sign(os.environ.get('username') , os.environ.get('password'), 0)
```

## 感谢
- 本项目完全建立在 [GenchAPI](https://pypi.org/project/GenchAPI/) 的基础上。
- 感谢 [Vincent Young](https://github.com/missuo) 对 [GenchAPI](https://pypi.org/project/GenchAPI/) 作出的贡献。
