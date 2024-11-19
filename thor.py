import ai2thor.controller

controller = ai2thor.controller.Controller()
controller.start()
controller.reset('FloorPlan1')
controller.step(dict(action='MoveAhead'))
controller.stop()
