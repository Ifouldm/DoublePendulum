# Double Pendulum
A visual representation and implementation of the double pendulum algorithm (https://en.wikipedia.org/wiki/Double_pendulum).

I was testing out various libraries for canvas drawings and wanted a short project to test out [PyGame](https://www.pygame.org/)

- [x] Display arm1 as line from pointA to pointB
- [x] Display arm1 as line from pointB to pointC
- [x] PointA is a fixed point
- [x] Display pointB as a circle of size relative to its mass
- [x] Display pointC as a circle of size relative to its mass
- [x] Implement algorithm to calculate new positions each frame
- [x] *Optionally display a trail behind pointB*

### Additional goals
The main goal was to understand and implement the alorithm which was completed but there are numerous other extra features which could be implemented such as:
- [ ] Colour
- [ ] Additional arms
- [ ] Controls for variables (starting points, arm lengths, point masses, friction etc)
- [ ] Draggable points
- [ ] Colour

## Dependencies

- [PyGame](https://www.pygame.org/)

## Images

![Double Pendulum](https://i.imgur.com/ISsDB0x.png "Double Pendulum Image")

## Run Application

```sh
python3 main.py
```
