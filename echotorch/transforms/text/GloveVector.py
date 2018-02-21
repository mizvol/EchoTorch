# -*- coding: utf-8 -*-
#

# Imports
import torch
import spacy
from datetime import datetime


# Transform text to word vectors
class GloveVector(object):
    """
    Transform text to word vectors
    """

    # Constructor
    def __init__(self, model="en_vectors_web_lg"):
        """
        Constructor
        :param model: Spacy's model to load.
        """
        # Properties
        self.model = model
        self.nlp = spacy.load(model)
    # end __init__

    ##############################################
    # Properties
    ##############################################

    # Get the number of inputs
    @property
    def input_dim(self):
        """
        Get the number of inputs.
        :return: The input size.
        """
        return 300
    # end input_dim

    ##############################################
    # Override
    ##############################################

    # Convert a string
    def __call__(self, text):
        """
        Convert a string to a ESN input
        :param text: Text to convert
        :return: Tensor of word vectors
        """
        # Inputs as tensor
        inputs = torch.FloatTensor(1, self.input_dim)

        # Start
        start = True
        count = 0

        # For each tokens
        for token in self.nlp(text):
            if not start:
                inputs = torch.cat((inputs, torch.FloatTensor(token.vector).unsqueeze_(0)), dim=0)
            else:
                inputs = torch.FloatTensor(token.vector).unsqueeze_(0)
                start = False
            # end if
            count += 1
        # end for

        return inputs, inputs.size()[0]
    # end convert

    ##############################################
    # Static
    ##############################################

# end GloveVector
