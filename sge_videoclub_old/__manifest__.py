# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Videoclub",
    "version": "16.0",
    "author": "Vanesa Espín",
    'summary': 'Videoclub creado para la clase de SGE',
    "license": "AGPL-3",
    "website": "https://github.com/OCA/server-tools",
    "category": "Tools",
    "depends": ["base"],
    "data": [
        "security/videoclub_security.xml",
        "security/ir.model.access.csv",      
        #"views/videoclub_view.xml",
    ],
    "application": True,
    "installable": True,
}
