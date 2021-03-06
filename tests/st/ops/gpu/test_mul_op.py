# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

import pytest
from mindspore import Tensor
from mindspore.ops import operations as P
import mindspore.nn as nn
import numpy as np
import mindspore.context as context


class NetMul(nn.Cell):
    def __init__(self):
        super(NetMul, self).__init__()
        self.mul = P.Mul()

    def construct(self, x, y):
        return self.mul(x, y)


@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.env_onecard
def test_mul():
    x0_np = np.random.uniform(-2, 2, (2, 3, 4, 4)).astype(np.float32)
    y0_np = np.random.uniform(-2, 2, (2, 3, 4, 4)).astype(np.float32)
    x1_np = np.random.uniform(-2, 2, (2, 3, 4, 4)).astype(np.float32)
    y1_np = np.random.uniform(-2, 2, (2, 1, 4, 4)).astype(np.float32)
    x2_np = np.random.uniform(-2, 2, (2, 1, 1, 4)).astype(np.float32)
    y2_np = np.random.uniform(-2, 2, (2, 3, 4, 4)).astype(np.float32)
    x3_np = np.random.uniform(-2, 2, 1).astype(np.float32)
    y3_np = np.random.uniform(-2, 2, 1).astype(np.float32)
    x4_np = np.array(768).astype(np.float32)
    y4_np = np.array(3072.5).astype(np.float32)

    x0 = Tensor(x0_np)
    y0 = Tensor(y0_np)
    x1 = Tensor(x1_np)
    y1 = Tensor(y1_np)
    x2 = Tensor(x2_np)
    y2 = Tensor(y2_np)
    x3 = Tensor(x3_np)
    y3 = Tensor(y3_np)
    x4 = Tensor(x4_np)
    y4 = Tensor(y4_np)

    context.set_context(mode=context.PYNATIVE_MODE, device_target="GPU")
    mul = NetMul()
    output0 = mul(x0, y0)
    expect0 = np.multiply(x0_np, y0_np)
    diff0 = output0.asnumpy() - expect0
    error0 = np.ones(shape=expect0.shape) * 1.0e-5
    assert np.all(diff0 < error0)
    assert (output0.shape() == expect0.shape)

    output1 = mul(x1, y1)
    expect1 = np.multiply(x1_np, y1_np)
    diff1 = output1.asnumpy() - expect1
    error1 = np.ones(shape=expect1.shape) * 1.0e-5
    assert np.all(diff1 < error1)
    assert (output1.shape() == expect1.shape)

    output2 = mul(x2, y2)
    expect2 = np.multiply(x2_np, y2_np)
    diff2 = output2.asnumpy() - expect2
    error2 = np.ones(shape=expect2.shape) * 1.0e-5
    assert np.all(diff2 < error2)
    assert (output2.shape() == expect2.shape)

    output3 = mul(x3, y3)
    expect3 = np.multiply(x3_np, y3_np)
    diff3 = output3.asnumpy() - expect3
    error3 = np.ones(shape=expect3.shape) * 1.0e-5
    assert np.all(diff3 < error3)
    assert (output3.shape() == expect3.shape)

    output4 = mul(x4, y4)
    expect4 = np.multiply(x4_np, y4_np)
    diff4 = output4.asnumpy() - expect4
    error4 = np.ones(shape=expect4.shape) * 1.0e-5
    assert np.all(diff4 < error4)
    assert (output4.shape() == expect4.shape)

    context.set_context(mode=context.GRAPH_MODE, device_target="GPU")
    mul = NetMul()
    output0 = mul(x0, y0)
    expect0 = np.multiply(x0_np, y0_np)
    diff0 = output0.asnumpy() - expect0
    error0 = np.ones(shape=expect0.shape) * 1.0e-5
    assert np.all(diff0 < error0)
    assert (output0.shape() == expect0.shape)

    output1 = mul(x1, y1)
    expect1 = np.multiply(x1_np, y1_np)
    diff1 = output1.asnumpy() - expect1
    error1 = np.ones(shape=expect1.shape) * 1.0e-5
    assert np.all(diff1 < error1)
    assert (output1.shape() == expect1.shape)

    output2 = mul(x2, y2)
    expect2 = np.multiply(x2_np, y2_np)
    diff2 = output2.asnumpy() - expect2
    error2 = np.ones(shape=expect2.shape) * 1.0e-5
    assert np.all(diff2 < error2)
    assert (output2.shape() == expect2.shape)

    output3 = mul(x3, y3)
    expect3 = np.multiply(x3_np, y3_np)
    diff3 = output3.asnumpy() - expect3
    error3 = np.ones(shape=expect3.shape) * 1.0e-5
    assert np.all(diff3 < error3)
    assert (output3.shape() == expect3.shape)

    output4 = mul(x4, y4)
    expect4 = np.multiply(x4_np, y4_np)
    diff4 = output4.asnumpy() - expect4
    error4 = np.ones(shape=expect4.shape) * 1.0e-5
    assert np.all(diff4 < error4)
    assert (output4.shape() == expect4.shape)
