# %%

# import pypi_downloads
# print(pypi_downloads.__version__)

from pypi_downloads import pypi_downloads
print(dir(pypi_downloads))

# %%
pp = pypi_downloads(username='erdogant')
# pp.update()
pp.stats(repo='bnlearn')
pp.stats(repo='distfit')
pp.stats(repo='worldmap')
pp.stats(repo='hnet')
pp.stats(repo='ismember')
pp.stats(repo='ismember')
pp.stats(repo='flameplot')
pp.stats(repo='pca')
pp.stats(repo='df2onehot')

# %%