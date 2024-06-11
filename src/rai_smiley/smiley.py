from importlib import resources as importlib_resources
from math import radians

import pandas as pd
import raimad as rai

from rai_smiley import resources

facial_data = pd.read_csv(
    importlib_resources.files(resources) / 'facial_data.csv'
    )

class Smiley(rai.Compo):
    """A smiley face component"""

    class Layers:
        face = rai.Layer(
            "The face layer"
            )
        eyes = rai.Layer(
            "The eyes layer"
            )
        mouth = rai.Layer(
            "The mouth layer"
            )

    class Options:
        happiness = rai.Option.Functional(
            "Happiness, from -10 to 10"
            )
        eye_size = rai.Option.Geometric(
            "Eye radius"
            )

    class Marks:
        left_eye = rai.Mark("Left eye center")
        right_eye = rai.Mark("Right eye center")

    def _make(self, eye_size: float = 5, happiness: float = 8):
        face = rai.Circle(50).proxy().map('face')
        eye_l = rai.Circle(eye_size).proxy().map('eyes')
        eye_r = eye_l.copy()

        smile = rai.AnSec(
            thetamid=radians(-90),
            dtheta=radians(abs(happiness) * 10),
            r1=40,
            r2=45
            ).proxy().map('mouth')

        if happiness < 0:
            smile.bbox.mid.hflip()

        eye_l.marks.center.to(
            face.bbox.interpolate(0.3, 0.7)
            )

        eye_r.marks.center.to(
            face.bbox.interpolate(0.7, 0.7)
            )

        smile.bbox.mid.to(
            face.bbox.interpolate(0.5, 0.2)
            )

        self.subcompos.face = face
        self.subcompos.eye_l = eye_l
        self.subcompos.eye_r = eye_r
        self.subcompos.smile = smile

        self.marks.left_eye = eye_l.bbox.mid
        self.marks.right_eye = eye_r.bbox.mid

