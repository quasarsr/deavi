/*
Copyright (C) 2016-2018 Quasar Science Resources, S.L.

This file is part of DEAVI.

DEAVI is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DEAVI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with DEAVI.  If not, see <http://www.gnu.org/licenses/>.
*/
AFRAME.registerPrimitive('a-ocean', {
    defaultComponents: {
        ocean: {},
        rotation: {x: -90, y: 0, z: 0}
    },
    mappings: {
        width: 'ocean.width',
        depth: 'ocean.depth',
        density: 'ocean.density',
        color: 'ocena.color',
        opacity: 'ocean.opacity'
    }
});
