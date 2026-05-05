import cclib
from cclib.parser import Gaussian
from pathlib import Path
from sys import argv, exit
import pandas as pd

for filename in Path.cwd().iterdir():
    if filename.is_file() and filename.suffix == '.log':
        mol = cclib.io.ccread(filename, format=Gaussian)
        assert len(mol.metadata['methods']) == 1 and mol.metadata['success'], "Log should contain one successful job."
        orbs = pd.DataFrame({'symmetry': mol.mosyms[0], 'energy': mol.moenergies[0]})
        orbs.loc[mol.homos[0]-1:mol.homos[0]+4].to_csv(filename.with_suffix('.csv'), index=False, header=None)

