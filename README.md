# 瓦片光照传播

一个在瓦片地图上算遮挡、并给出逐格光照强度的传播器

## 保留签名

- `TileMap`
- `propagate(map, lights)`
- `occluders(map, x, y)`
- `attenuation(dist)`

## 自测

```
python -m pytest tests -q
python -m tilelight.cli data/tilemap.txt --out light.txt
```
