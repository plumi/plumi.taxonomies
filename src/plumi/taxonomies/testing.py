from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import plumi.taxonomies


PLUMI_TAXONOMIES = PloneWithPackageLayer(
    zcml_package=plumi.taxonomies,
    zcml_filename='testing.zcml',
    gs_profile_id='plumi.taxonomies:testing',
    name="PLUMI_TAXONOMIES")

PLUMI_TAXONOMIES_INTEGRATION = IntegrationTesting(
    bases=(PLUMI_TAXONOMIES, ),
    name="PLUMI_TAXONOMIES_INTEGRATION")

PLUMI_TAXONOMIES_FUNCTIONAL = FunctionalTesting(
    bases=(PLUMI_TAXONOMIES, ),
    name="PLUMI_TAXONOMIES_FUNCTIONAL")
