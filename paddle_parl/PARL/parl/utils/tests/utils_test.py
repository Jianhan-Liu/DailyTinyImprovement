#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import unittest
from parl.utils import action_mapping


class TestUtils(unittest.TestCase):
    def test_action_mapping(self):
        origin_act = np.array([-1.0, 0.0, 1.0])

        mapped_act = action_mapping(origin_act, 0.0, 1.0)
        self.assertListEqual(list(mapped_act), [0.0, 0.5, 1.0])

        mapped_act = action_mapping(origin_act, -2.0, 2.0)
        self.assertListEqual(list(mapped_act), [-2.0, 0.0, 2.0])

        mapped_act = action_mapping(origin_act, -5.0, 10.0)
        self.assertListEqual(list(mapped_act), [-5.0, 2.5, 10.0])


if __name__ == '__main__':
    unittest.main()
