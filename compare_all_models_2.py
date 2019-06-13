#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Basic example which iterates through the tasks specified and runs the given
model on them.

Examples
--------

.. code-block:: shell

  python examples/display_model.py -t babi:task1k:1 -m "repeat_label"
  python examples/display_model.py -t "#MovieDD-Reddit" -m "ir_baseline" -mp "-lp 0.5" -dt test
"""  # noqa: E501

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task

import json

import random


def setup_args():
    parser = ParlaiParser(True, True, 'Display model predictions.')
    parser.add_argument('-n', '--num-examples', default=10)
    parser.add_argument('--display-ignore-fields', type=str, default='')
    # by default we want to display info about the validation set
    parser.set_defaults(datatype='valid')
    return parser


def display_model(opt):
    random.seed(42)

    import os
    cwd = '/'.join(os.getcwd().split('\\')[:-1])+'/trained/twitter/'
    model_files = [mf for mf in os.listdir(cwd) if os.path.isdir(cwd+mf)]
    agents = []
    for mf in model_files:
        # opt['override']['model_file'] = "../trained/twitter/" + mf + '/' + mf
        opt['model_file'] = "../trained/twitter/" + mf + '/' + mf
        opt['face_instance'] = mf

        agents.append(create_agent(opt, requireModelExists=True))
    world = create_task(opt, agents)

    # Show some example dialogs.
    with world:
        for _k in range(int(opt['num_examples'])):
            world.parley()
            print(world.display() + "\n~~")
            if world.epoch_done():
                print("EPOCH DONE")
                break


if __name__ == '__main__':
    # Get command line arguments
    parser = setup_args()
    opt = parser.parse_args()
    display_model(opt)
