# coding: utf-8

"""
    Un tokenizer cree specifiquement pour les messages postes sur Twitter (appeles tweets).
    Les contraintes imposees par Twitter lors de la redaction des messages forcent les 
    utilisateurs a ne pas suivre les standards typographiques.
    Le but de ce tokenizer est de reduire au maximum le bruit induit par les contraintes
    tout en conservant un maximum des informations disponibles dans le tweet.
"""

from .tokenizer import Tokenizer
