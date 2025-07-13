# Typer

## Official Website

<https://typer.tiangolo.com/>

## Example Code

### hello_typer.py

Typer會自動生成help，help會帶出function的argument等等資訊。可以試試看在自己的CLI上面打打看下面這行指令。

```shell
python hello_typer.py --help
```

![help_example](.\artifects\imgs\help_example.png)

### more_command.py

如果說有多個function都加上@app.command()的decorator的話，打上```python more_command.py --help```的話，會列出所有可執行的command選項。
![more_command](.\artifects\imgs\more_command.png)

