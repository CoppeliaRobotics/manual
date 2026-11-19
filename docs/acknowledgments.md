# Acknowledgments and credits

CoppeliaSim/V-REP was developed during several years, however, without the contributions, help, support, advice, or generosity of many people, it wouldn't have become what it is today. We thank and acknowledge the contributions in various forms of the following people, group of people or organizations:

- Nobuto Matsuhira (Toshiba Corporate R&D center), for the enormous support, belief in me, and kindness he always showed me
- Fumio Ozaki (Toshiba Corporate R&D center), for the patience, trust and freedom he gave me
- Hoimin Jeong (Cubictek Co. Ltd), for his support and belief in me even in difficult situations
- The Lua development team (PUC-Rio, [http://www.lua.org](http://www.lua.org)), for the free Lua interpreter they provide. [See the license](#LuaCredit).
- Nokia corporation, the Qt GUI Toolkit development team and all other contributors, for the [Qt GUI Toolkit](http://www.qt.nokia.com) library they provide. [See the license](#QtCredit).
- Digia Plc and/or its subsidiary(-ies), and all other contributors, for the [Qt Property Browser](http://qt.gitorious.org/qt-solutions/qt-solutions/trees/master/qtpropertybrowser) they provide. [See the license](#QtPropertyBrowserCredit).
- Antonio Escano Scuri and Mark Stroetzel Glasberg for the free WebBook framework they provide. [See the license](#WebBookCredit).
- Diego Nehab ([http://w3.impa.br/~diego/software/luasocket/home.html](http://w3.impa.br/~diego/software/luasocket/home.html)), for the free LuaSocket extension library. [See the license](#LuaSocketCredit).
- Erwin Coumans ([http://www.bulletphysics.org](http://www.bulletphysics.org)), for the [Bullet physics library](dynamicsModule.md#bullet) he provides. [See the license](#BulletCredit).
- The team behind [MuJoCo](https://mujoco.org/), for the physics library they provide. [See the license](#mujoco).
- Russel L. Smith ([http://www.ode.org](http://www.ode.org)), for the physics library he provides. [See the license](#OdeCredit).
- Daniel Fiser for his collision routines (libccd, used with [ODE](dynamicsModule.md#ode)). [See the license](#collisionLibccdCredit).
- Samuel Cavalcanti for his Rust ZeroMQ remote API client. [See the license](#rust).
- Pierre Terdiman for his collision routines (OPCODE, used with [ODE](dynamicsModule.md#ode)).
- Francisco Leon Najera for his collision routines (GIMPACT, used with [Bullet](dynamicsModule.md#bullet)). [See the license](#collisionGimpactCredit).
- The people and community behind the [Open Motion Planning Library (OMPL)](http://ompl.kavrakilab.org). [See the license](#ompl).
- Khaled Mamou, for the excellent convex decomposition routines he provides (HACD and V-HACD). [See the license](#convexCredit).
- Brad Barber, for the efficient Qhull routines he provides. [See the license](#convexHullCredit).
- Oliver Gay and Zedwood.com, for their sha256 implementation. [See the license](#sha256).
- François Conti, for the CHAI3D library he provides. [See the license](#CHAI3D).
- The Scintilla development team ([http://www.scintilla.org](http://www.scintilla.org)), for the free source code editing component they provide. Since CoppeliaSim 2.6.0, the Scintilla library is used via [commercial QScintilla](http://www.riverbankcomputing.com).
- Lee Thomason, for his nice and compact tinyxml routines. [See the license](#tinyxmlCredit).
- Marcus Geelnard for the Basic Compression Library he provides ([http://bcl.comli.eu/home-en.html](http://bcl.comli.eu/home-en.html)). [See the license](#BasicCompressionLibrary).
- Toni Ronkko for the Dirent interface for Microsoft Visual Studio he provides ([https://github.com/tronkko/dirent](https://github.com/tronkko/dirent)). [See the license](#Dirent).
- Martin Courchesne and [SimWat](http://www.simwat.com/) for the initial [Vortex plugin](dynamicsModule.md#vortex) for CoppeliaSim they provided.
- [CM Labs](http://www.cm-labs.com) for the free version of their Vortex physics engine ([Vortex Studio](https://www.cm-labs.com/vortex-studio/)), used in CoppeliaSim's Vortex plugin.
- Sean Barrett for his image loading routines he provides.
- Jari Komppa for the [ESCAPI library](http://sol.gfxile.net/escapi/index.html) that is wrapped in the webcam plugin for CoppeliaSim (Credit is given when the plugin is used)
- Julio Jerez and Alain Suero, for the [Newton plugin](dynamicsModule.md#newton) for CoppeliaSim they provide. [See the license](#newtonCredit).
- René Nyffenegger, for the base64 source code he provides. [See the license](#base64Credit).
- The programming community on [http://www.gamedev.net](http://www.gamedev.net) and [http://www.codeproject.com](http://www.codeproject.com) for the many invaluable advices, tips and code snippets
- The developers of the [FFmpeg library](http://www.ffmpeg.org) and Andrew Voznytsa who wrote a library for CoppeliaSim that offers video compression functionality based on FFmpeg. [See the FFmpeg license](#ffmpegCredit).
- The Computer Graphics Group at RWTH Aachen, who developed the [OpenMesh](http://www.openmesh.org) library. The library is used in the CoppeliaSim plugin [simOpenMesh](https://github.com/CoppeliaRobotics/simOpenMesh). [See the OpenMesh license](#openMeshCredit).
- The team behind the [Assimp library](http://www.assimp.org/). The library is used in the CoppeliaSim plugin [simAssimp](https://github.com/CoppeliaRobotics/simAssimp). [See the Assimp license](#assimpCredit).
- Torsten Kroeger and [Reflexxes GmbH](http://www.reflexxes.com), for providing their [Reflexxes Motion Library type II](http://www.reflexxes.com/products/reflexxes-motion-libraries) as a CoppeliaSim plugin. [See the RML Type II license](#reflexxes).
- Lars Berscheid, for providing his [Ruckig Online Trajectory Generator](https://github.com/pantor/ruckig#readme) as a CoppeliaSim plugin. [See the Ruckig license](#ruckig).
- Chris Hecker for his mass properties calculation algorithm. [See the related license](#chrisHecker).
- Christian Dippel, my cousin, who helped me in many ways (CAD models, flyer preparation, etc.)
- Michele Guarnieri, Paulo Debenest and Naho Guarnieri from Hibot, who are not only my partners in Business, but also friends.
- Lyall Randell who not only gave me permission to use his CAD models, but also created additional ones especially for CoppeliaSim.
- Eric Rohmer who is a thorough CoppeliaSim tester and an "idea machine". He is also the creator of several models and plugins for CoppeliaSim (e.g. simExtWii or simExtJoystick)
- Svetlin Penkov for creating a first ROS plugin, and for being always available for ROS-related questions.
- Ignacio Tartavull for creating a first URDF plugin, and for being extremely helpful at the right time.
- Maciej Szymanski, Ibrahim Abd Elkader, Mahendra Koteshwar and Asanka Wickramasinghe for various tasks in relation with CoppeliaSim porting and legacy remote API bindings
- Julien Tharin for various tasks in relation with CoppeliaSim porting
- Preben Hjornet for creating precise simulation models of extremely complex robots
- "gl.tter" for the WiiYourself! wiimote code ([http://gl.tter.org](http://gl.tter.org)) wrapped in the wiiMote plugin for CoppeliaSim (Credit is given when the plugin is used).
- Alex Doumanoglou for writing the Collada importer/exporter plugin.
- Cedric Pradalier for extending the RosPlugin with useful publisher/subscriber types.
- Andreas Geiger, for the [LIBICP](http://www.cvlibs.net/software/libicp/) he provides. [See the license](#icp).
- Hung Pham, Quang Cuong Pham and others, for the [TOPP-RA](https://hungpham2511.github.io/toppra/) library they provide. [See the license](#toppra).
- Diego Daniel Santiago for writing a shared memory communication plugin, and the [plugin for Simulink-CoppeliaSim communication](https://github.com/santdiego/simExtSimulink).
- The developers of the POV-Ray raytracer, Persistence of Vision Raytracer Pty. Ltd. POV-Ray uses the [GNU AFFERO GENERAL PUBLIC LICENSE](http://www.povray.org/povlegal.html), a copy of which is included in the software package.
- The developers of the [CGAL library](http://www.cgal.org/), which is used by the *simSurfRec* plugin. [See the license](#CGAL).
- The developers of [LIBIGL](https://libigl.github.io/), which is wrapped in the IGL plugin. [See the license](#IGL).
- The developers of [ZeroMQ](https://zeromq.org/), which is wrapped in several CoppeliaSim plugins, and used in several external applications. [See the license](#ZMQ).
- The developers of [WebSocket++](https://www.zaphoyd.com/projects/websocketpp/), which is wrapped in the WS plugin. [See the license](#WS).
- The developers of [three.js](https://threejs.org/), which is user by CoppeliaSim's external viewer. [See the license](#threejs).
- The developers of [highlight.js](https://highlightjs.org/), a syntax highlighting library used in CoppeliaSim's manual and in the Coppelia Robotics forums. [See the license](#hljs).
- Christoph Kubisch, the developer of [ldrawloader](https://github.com/pixeljetstream/ldrawloader). [See the license](#ldraw).
- All the developers behind the [OpenCV](https://opencv.org) library, which is used by the *simIM* plugin. [See the license](#openCv).
- David Heiko Kolf, for [his JSON module for Lua](http://dkolf.de/src/dkjson-lua.fsl/home). [See the license](#json).
- Francois Perrad, for [his MessagePack module for Lua](https://github.com/fperrad/lua-MessagePack). [See the license](#messagePack-lua).
- Takatoshi Kondo and several other contributors, for [their MessagePack code for C/C++](https://github.com/msgpack/msgpack-c). [See the license](#messagePack-c).
- Bastian Bechtold, for [his MessagePack code for Matlab](https://github.com/bastibe/matlab-msgpack). [See the license](#messagePack-matlab).
- The people behind the [MessagePack code for Java](https://github.com/msgpack/msgpack-java). [See the license](#messagePack-java).
- Kim Alvefur, for [his CBOR code for Lua](https://www.zash.se/lua-cbor.html). [See the license](#cbor-lua).
- Sean Conner, for [his CBOR library for Lua](https://github.com/spc476/CBOR). [See the license](#cbor-lua2).
- Federico Ferri, for creating a whole series of plugins for CoppeliaSim.
- Stephen James (Imperial College London) for his [PyRep toolkit for robot learning research](https://github.com/stepjam/PyRep), and his [simOpenGL3 plugin](https://github.com/coppeliaRobotics/simOpenGL3).
- Emanuel Eichhammer, for his [QCustomPlot](http://www.customplot.com) used in the [custom UI plugin](customUIPlugin.md). [See the license](#qcustomplot).
- Marcin Konarski, Salvatore Sanfilippo, Pieter Noordhuis for the [Replxx](https://github.com/AmokHuginnsson/replxx/) library, used in the headless version of the [commander plugin](commandLine.md#commander). [See the license](#replxx).
- Benjamin Navarro, for his code in the legacy remote API, which enables shared memory communication instead of socket communication.
- Enrique García Cota, for his "middleclass" OOP library for Lua.
- Following people for noticing bugs, reporting problems, suggesting solutions or new ideas, providing patches, code improvements, or simply helping out: Bejade Choy, Farkas Gergo, Barry van de Laar, Lucia Teglas, Casper Christensen, Andrew Alexander, Kazuyuki Shigeto, Joost a.k.a. J-m@n, Bjorn Kilen, Andrés San Millán Rodriguez, Mey Lean Kronemann, Marco Cognetti, Tesuno Tokisin, Guillermo Presti, Matthias Fueller, Paul Fudal, Matthieu Lapeyre, Alberto Fanjul, Laurens Philippo, Vadim Liventsev, Kirill Makukhin, Patrick Bouffard, Pouya Mohammadi, Luca Marchionni, Barrett Ames, Arnaud Leleve, Geerten Doornenbal, Nikolaus Wittenstein, Ayberk Ozgur, Qi Wang, Giordano, Karl Robillard, Brian Yeomans, Kiyoshi Irie, Ulrich Schwesinger, Peter Mačička, Inkyu Sa, David Butterworth, Marco Cognetti, Xinyu Zhang, Jaqueline Gallardo, Serkan ÇİÇEK, Taehoon Koo, He Tao, Yusuke Ishizawa, Billy Newman, Rüdiger Dehmel, Roberto Marino, Renaud Detry, Roband, Hendrik Wiese, Matthias Schindler, George Moustris, Marco Bellaccini, Klaus Raizer, Paulo Gurgel, Stéphane Magnenat, Philipp Krüsi, Pascal Gohl, Gianpaolo Gonnelli, Felix Herrmann, Edgar Virga, Josep Tormo Costa, Gaël Ecorchard, Massimo Cefalo, Robert Lang, Marc Durvaux, Alexander Rietzler, Matt Derry, Arne Hitzmann, Sergi Foix, Daniel Morberg, Andreas Kuhner, Gerold Huber, Danilo Vasconcellos Vargas, Spencer Krause, Daniel Kuhner, Filip Jares, Luigi Ferri, Michaela Richter, Daniel Lechner, Sven Knüppel, Steve Nguyen, Jonas Sperling, Roberto Guzman, James Besancon, Andrew Vardy, Bipeen Acharya, Fred Gisa, Simon D. Levy, Leopoldo Armesto, Rodrigo Moreno Garcia, Hanna Kurniawati, Dimitri Klimenko, Joshua Mun Song, Vinay Yadav, Thomas Estier, Matthias Imle, Rosé Rosado, Soner Ulun, Reza Mahjourian, Ben Allan, Riccardo Spica, Giovanni Claudio, Guenter Schreiber, Antoine Rennuit, Francois Conti, Sébastien Granges, Patrick Helmer, Eva Alves Costa, Lucian Cucu, Sigurd Villumsen, Andrea Censi, Pierre Rouanet, Leander Hille, Christoph Hügle, William Harrison, Scott Drew Pendleton, Jan Dentler, Raimund Krenmüller, Anuraj Rajendraprakash, Ilya Nemihin, Ángel Luis Jiménez García, Leander Hille, Pierre Rouanet, Kenichi Hara, Ilya Nemihin, Federico Ferri, Michael Michalik, Martin Pecka, Nicola Piccinelli, Kshitij Tiwari, Victor Gomez, Parker Owan, Yuki Suga, Muhammad Umer Huzaifa, Marshall Floyd, Augusto Gandia, Pierre Jacquot, Gurvan Le Bleis, Andreu Vidal, Nicola Di Pol, Tobias Groll, Wu Xiaojun, Karol Mocniak, Ana Lucia, Ricardo Azambuja, Anto Ronson, Graeme Neff Wilson, Minson Lee, Tiago Malheiro, Andrew Hundt, Ahmed Yacine, Matthias Ploner, Indranil Sur, Sung Kyun Kim, Rik Timmers, Matthew Veres, Korolyov Alexei, Daniel Angelov, Mohammed Talha, Bartolomeo Della Corte, Scott Hissam, Mark Fink, Hao Wang, Matias Nitsche, Ndivhuwo Makondo, Yu Zhang, DeKita G. Moon, Paul Santiago Tumbaco Casa, Tobias Benz, Rodrigo Moreno Garcia, Arjun Narayanan, Sven Schweigler, Nicola Battilani, Mark Edmonds, Benno Timmermann, Cándido Otero Moreira, Justin Yim, Allen Zhu, Leo Koppel, Ravi Prakash Joshi, Sina Radmard, Sai Vemprala, Waleed El-Badry, James Barger, Gonzalo Casas, Metehan Doyran, Arif Rahman, Jason Cachrane, Steffen Hemer, Fangyi Zhang, Filipe Rocha, virgile Daugé, Riccardo Spica, Florian Golemo, Kevin M. Lynch, Frank C. Park, Jacob Huesman, Matthew Veres, Cándido Otero, Leon Masopust, Michael Tong, Zhengxing Yang, Thomas Gurriet, Lenka Pitonakova, Hervé Frezza-Buet, Justus Rijke, Stefan Müller, Julien Lechalupe, Tristan Gahler, Robert Peck, William Jones, Benjamin Erdemann, Boris Bogaerts, Ulrich Viereck, Amdrei Florea, Catalin Buiu, Joachim Haensel, Julian Mayer, Jacob Smith, Mohsen Moradi Dalvand, Simon Birrell, Mathias Thor, Jedrzej Orbik, Liu Dong, Mark Hartenstein, Alexander Oliva, Claudio Gaz, Simon Birrell, Sahil Sharma, Adrian Schoisengeier, Rémi Lux, Kilian Freitag, Maël Hörz, Jakub Turaj, Rieky Barady, Jian Ye, Jaime Boal, Pável Axel Mc Campos Peña, Patrick Gruener, Thomas Wilmotte, Lorenzo Romanini, Johan Relefors, Pablo Bustos, Sonny Tarbouriech, Aleksander Sil, Arturs Paugurs, Wei Wei, David Page, Leopoldo Armesto, Ayush Patel, Cameron Kabacinski, Francisco Marin, Kevin Thomas, Nikita Aigner, Charles Han, Shai Levy, Bobovsky Zdenko, Salvatore Sessa, Jakob Ambsdorf, Hayato Amaike, Nathan Kocherhans, Alex Wuqi Zhang, René Simon, Yongdong Wang, Andrés Faíña, Davide Scorza, Jovan Sumarac, Alexander Oliva, Luigi Ascione, Rui Li, Patrick Grüner, Andrés Faíña, Michal Mareš, Kat Styles Wood, David Paulius, Pranav A. Bhounsule, Davide Scorza, Amirhossein Afkhami Ardekani, Roman Horshkov, Volker Kühn, Artem Shishkin, Andrey Voronkov, Vitalii Kudinov, Yong Jiang, Marco Frigerio, Elia Cereda, Keith Siilats, Pardeep Singh Panesar, Zichun Xu, Belal Elsayed, Clélie Demey, Fumio Ozaki, Christopher Blum, Javier Quintana, Alexis Hou, Sebastian Serna, Jian Qi, Vishwas Jain, Barca David, Sasha Koryakin, Louis Munier, Fatih Kocyigit, Clément Moulin-Frier, Markus Voelk, Fabio Massimo Proietti, Michael Leslie, Cheng Zhou, Ben Figg, Caio Conti Guidote Ribeiro, Daniel Schiller, Juan José Quiroz Omaña, Matteo Nini, Philippe Juhel, Jeffrey W. Herrmann, Sinan Barut, Javier Lopez, Jonatas Teixeira, github user MoonNarga, *Riften*, Congjun Ma, Wilbert Pumacay, Ziwen Zhao, Hannes Weixler, Matt Pearson... We know we forgot many many people, also significant ones... please let us know!

We also thank following people for the inspiration they provided in various fields through their publications, books or other means:

- J. J. Kuffner Jr., S.M. LaValle, L. Sciavicco, B. Siciliano, S. Gottschalk, M. C. Lin, D. Manocha, T. Akenin-Moeller

See also [this licensing overview page](licensing.md).

## <a id="LuaCredit"></a>License of the Lua script interpreter

License for Lua 5.0 and later versions

Copyright © 1994-2008 Lua.org, PUC-Rio.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="WebBookCredit"></a>License of the WebBook framework

Copyright 1994-2009 Tecgraf / PUC-Rio.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="LuaSocketCredit"></a>License of the LuaSocket extension library

License for LuaSocket 2.0.2

Copyright © 2004-2007 Diego Nehab. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="BulletCredit"></a>License of the Bullet Physics Library

Bullet Continuous Collision Detection and Physics Library

Copyright (c) 2003-2006 Erwin Coumans http://continuousphysics.com/Bullet/

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software. Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1\. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

2\. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3\. This notice may not be removed or altered from any source distribution.

## <a id="mujoco"></a>License of the MuJoCo Physics Library

The library is licensed under the Apache Licnese version 2.0

http://www.apache.org/licenses/

## <a id="OdeCredit"></a>License of the Open Dynamics Engine

Open Dynamics Engine

Copyright (c) 2001-2004, Russell L. Smith.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

Neither the names of ODE's copyright owner nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="collisionLibccdCredit"></a>License of the Libccd routines

\* Copyright (c)2010 Daniel Fiser &lt;danfis at danfis dot cz>
\*
\*
\* This file is part of libccd.
\*
\* Distributed under the OSI-approved BSD License (the "License");
\* see accompanying file BDS-LICENSE for details or see
\* &lt;http://www.opensource.org/licenses/bsd-license.php>.
\*
\* This software is distributed WITHOUT ANY WARRANTY; without even the
\* implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
\* See the License for more information.

## <a id="rust"></a>License of the Rust ZeroMQ remote API

BSD 2-Clause License
Copyright (c) 2022, Samuel Cavalcanti All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1\. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2\. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="collisionGimpactCredit"></a>License of the GIMPACT routines

Copyright (c) 2006 Francisco Leon Najera. C.C. 80087371.
email: projectileman at yahoo dot com

This library is free software; you can redistribute it and/or
modify it under the terms of EITHER:
(1) The GNU Lesser General Public License as published by the Free
Software Foundation; either version 2.1 of the License, or (at
your option) any later version. The text of the GNU Lesser
General Public License is included with this library in the
file GIMPACT-LICENSE-LGPL.TXT.
(2) The BSD-style license that is included with this library in
the file GIMPACT-LICENSE-BSD.TXT.
(3) The zlib/libpng license that is included with this library in
the file GIMPACT-LICENSE-ZLIB.TXT.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the files
GIMPACT-LICENSE-LGPL.TXT, GIMPACT-LICENSE-ZLIB.TXT and GIMPACT-LICENSE-BSD.TXT for more details.

## <a id="convexCredit"></a>License of the convex decomposition routines

Copyright (c) 2011 Khaled Mamou (kmamou at gmail dot com)
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1\. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2\. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3\. The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="convexHullCredit"></a>License of the Qhull routines

Qhull, Copyright (c) 1993-2012
C.B. Barber
Arlington, MA
and
The National Science and Technology Research Center for
Computation and Visualization of Geometric Structures
(The Geometry Center)
University of Minnesota
email: qhull at qhull dot org
This software includes Qhull from C.B. Barber and The Geometry Center.
Qhull is copyrighted as noted above. Qhull is free software and may
be obtained via http from www.qhull.org. It may be freely copied, modified,
and redistributed under the following conditions:
1\. All copyright notices must remain intact in all files.
2\. A copy of this text file must be distributed along with any copies
of Qhull that you redistribute; this includes copies that you have
modified, or copies of programs or other software products that
include Qhull.
3\. If you modify Qhull, you must include a notice giving the
name of the person performing the modification, the date of
modification, and the reason for such modification.
4\. When distributing modified versions of Qhull, or other software
products that include Qhull, you must provide notice that the original
source code may be obtained as noted above.
5\. There is no warranty or other guarantee of fitness for Qhull, it is
provided solely "as is". Bug reports or fixes may be sent to
qhull_bug at qhull dot org; the authors may or may not act on them as
they desire.

## <a id="sha256"></a>License of the sha256 implementation

Updated to C++, zedwood.com 2012
Based on Olivier Gay's version
See Modified BSD License below:
FIPS 180-2 SHA-224/256/384/512 implementation
Issue date: 04/30/2005
http://www.ouah.org/ogay/sha2/
Copyright (C) 2005, 2007 Olivier Gay &lt;olivier.gay@a3.epfl.ch>
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1\. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2\. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3\. Neither the name of the project nor the names of its contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS \`\`AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

## <a id="tinyxmlCredit"></a>License of the tinyxml routines

Original code by Lee Thomason (www.grinninglizard.com)

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any
damages arising from the use of this software.

Permission is granted to anyone to use this software for any
purpose, including commercial applications, and to alter it and
redistribute it freely, subject to the following restrictions:

1\. The origin of this software must not be misrepresented; you must
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2\. Altered source versions must be plainly marked as such, and
must not be misrepresented as being the original software.

3\. This notice may not be removed or altered from any source
distribution.

## <a id="ffmpegCredit"></a>License of the FFmpeg library

CoppeliaSim is linking dynamically to a library that itself links to the unmodified FFmpeg library files. The unmodified FFmpeg library, source and binaries (as distributed with CoppeliaSim), is available for download from [here](http://www.ffmpeg.org)

FFmpeg is licensed under the [GNU Lesser General Public License (LGPL) version 2.1](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) or later. However, FFmpeg incorporates several optional parts and optimizations that are covered by the [GNU General Public License (GPL) version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html) or later. If those parts get used the GPL applies to all of FFmpeg.

## <a id="openMeshCredit"></a>License of the OpenMesh library

OpenMesh makes use of the [LGPL v3](https://www.gnu.org/licenses/lgpl.html) with the following exception:
As a special exception to the GNU Lesser General Public License, you may use any file of this software library without restriction. Specifically, if other files instantiate templates or use macros or inline functions from this file, or you compile this file and link it with other files to produce an executable, this file does not by itself cause the resulting executable to be covered by the GNU Lesser General Public License. This exception does not however invalidate any other reasons why the executable file might be covered by the GNU Lesser General Public License.

## <a id="assimpCredit"></a>License of the Assimp library

Assimp makes use of a 3-clauses BSD license:

Copyright (C) 2006-2015 assimp team, All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of the assimp team nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="QtCredit"></a>License of the Qt GUI Toolkit library

CoppeliaSim is linking dynamically to the unmodified Qt library.

The Qt GUI Toolkit is Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
Contact: Nokia Corporation (qt-info at nokia dot com)

Qt is available under the LGPL version 2.1 (GNU Lesser General Public License version 2.1).

## <a id="QtPropertyBrowserCredit"></a>License of the Qt Property Browser

Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies). Contact: http://www.qt-project.org/legal

This file is part of the Qt Solutions component. You may use this file under the terms of the BSD license as follows:

"Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

\* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

\* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

\* Neither the name of Digia Plc and its Subsidiary(-ies) nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."

## <a id="BasicCompressionLibrary"></a>License of the Basic Compression Library

Copyright © 2003-2006 Marcus Geelnard

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1\. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

2\. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3\. This notice may not be removed or altered from any source distribution.

## <a id="CHAI3D"></a>License of the CHAI3D Library

Software License Agreement (BSD License)
Copyright (c) 2003-2014, CHAI3D.
(www.chai3d.org)

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

\* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

\* Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided
with the distribution.

\* Neither the name of CHAI3D nor the names of its contributors may
be used to endorse or promote products derived from this software
without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="chrisHecker"></a>License of the mass properties calculation algorithm

This code computes volume integrals needed for determining mass properties of polyhedral bodies.

For more information, see the accompanying README file, and the paper

Brian Mirtich, "Fast and Accurate Computation of Polyhedral Mass Properties," journal of graphics tools, volume 1, number 1, 1996.

This source code is public domain, and may be used in any way, shape or form, free of charge.

Copyright 1995 by Brian Mirtich

mirtich at cs dot berkeley dot edu
http://www.cs.berkeley.edu/~mirtich

## <a id="newtonCredit"></a>License of Newton Dynamics

Newton is licensed under the liberal zlib open source license, with little if any practical difference between them.

Copyright (c) &lt;2003-2011>

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1\. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.

2\. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

3\. This notice may not be removed or altered from any source distribution.

Julio Jerez and Alain Suero

## <a id="Dirent"></a>License of the Dirent interface

Dirent interface for Microsoft Visual Studio

Version 1.21

Copyright (C) 2006-2012 Toni Ronkko

This file is part of dirent. Dirent may be freely distributed under the MIT license. For all details and documentation, see https://github.com/tronkko/dirent

## <a id="CGAL"></a>License of the CGAL library

(the unmodified CGAL shared library is used by the simSurfRec plugin)

Some parts of CGAL are available under the [LGPL](http://www.gnu.org/copyleft/lesser.html), other parts are under the [GPL](http://www.gnu.org/copyleft/gpl.html). For details see [here](http://www.cgal.org/license.html) and also refer to the LICENSE file from the CGAL source code distribution.

## <a id="IGL"></a>License of Libigl

Libigl is primarily licensed under MPL2. For details see [here](https://libigl.github.io/license/).

## <a id="ZMQ"></a>License of ZeroMQ

ZeroMQ Free Software Licenses

The libzmq library is licensed under the [GNU Lesser General Public License](http://www.gnu.org/licenses/lgpl.html) V3 plus a static linking exception.

\- **You get the full source code**. You can examine the code, modify it, and share your modified code under the terms of the LGPL.

\- **Static linking exception**. The copyright holders give you permission to link this library with independent modules to produce an executable, regardless of the license terms of these independent modules, and to copy and distribute the resulting executable under terms of your choice, provided that you also meet, for each linked independent module, the terms and conditions of the license of that module. An independent module is a module which is not derived from or based on this library. If you modify this library, you must extend this exception to your version of the library.

## <a id="WS"></a>License of WebSocket++

Copyright (c) 2014, Peter Thorson. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

\* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

\* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

\* Neither the name of the WebSocket++ Project nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PETER THORSON BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Detailed related to the bundled libraries can be found [here](https://github.com/zaphoyd/websocketpp/blob/master/COPYING)

## <a id="threejs"></a>License of three.js

The MIT License

Copyright © 2010-2022 three.js authors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="hljs"></a>License of highlight.js

BSD 3-Clause License

Copyright (c) 2006, Ivan Sagalaev.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

\* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

\* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

\* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="ldraw"></a>License of ldrawloader

MIT License

Copyright (c) 2019-2020 Christoph Kubisch

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="json"></a>License of the dkjson module for Lua

Copyright (C) 2010-2014 David Heiko Kolf

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="messagePack-lua"></a>License of the MessagePack module for Lua

Copyright (c) 2012-2018 Francois Perrad

This library is licensed under the terms of the MIT/X11 license, like Lua itself:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="messagePack-c"></a>License of the MessagePack code for C/C++

Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization obtaining a copy of the software and accompanying documentation covered by this license (the "Software") to use, reproduce, display, distribute, execute, and transmit the Software, and to prepare derivative works of the Software, and to permit third-parties to whom the Software is furnished to do so, all subject to the following:

The copyright notices in the Software and this entire statement, including the above license grant, this restriction and the following disclaimer, must be included in all copies of the Software, in whole or in part, and all derivative works of the Software, unless such copies or derivative works are solely in the form of machine-executable object code generated by a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="messagePack-matlab"></a>License of the MessagePack code for Matlab

Copyright (c) 2014 Bastian Bechtold

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1\. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2\. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3\. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="messagePack-java"></a>License of the MessagePack code for Java

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## <a id="cbor-lua"></a>License of Lua-CBOR

Copyright (c) 2014-2015 Kim Alvefur

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="cbor-lua2"></a>License of org.conman.cbor

The library is licensed under [LGPL V3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)

## <a id="qcustomplot"></a>License of QCustomPlot

Coppelia Robotics AG uses a commercial license of QCustomPlot

QCustomPlot is licensed under the [GNU General Public License (GPL)](http://www.gnu.org/licenses/gpl.html). See also *GPL.txt* located in the project files of the [custom UI plugin](customUIPlugin.md) ([simUI](https://github.com/CoppeliaRobotics/simUI)).

## <a id="icp"></a>License of LibICP

Copyright 2011. All rights reserved.
Institute of Measurement and Control Systems
Karlsruhe Institute of Technology, Germany

Authors: Andreas Geiger

libicp is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation; either version 3 of the License, or any later version.

libicp is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
libicp; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA 02110-1301, USA

## <a id="base64Credit"></a>License of base64 source code

base64.cpp and base64.h
base64 encoding and decoding with C++.
Version: 1.01.00

Copyright (C) 2004-2017 René Nyffenegger

This source code is provided 'as-is', without any express or implied
warranty. In no event will the author be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1\. The origin of this source code must not be misrepresented; you must not
claim that you wrote the original source code. If you use this source code
in a product, an acknowledgment in the product documentation would be
appreciated but is not required.
2\. Altered source versions must be plainly marked as such, and must not be
misrepresented as being the original source code.
3\. This notice may not be removed or altered from any source distribution.

René Nyffenegger rene.nyffenegger@adp-gmbh.ch

## <a id="openCv"></a>License of OpenCV

License Agreement
For Open Source Computer Vision Library
(3-clause BSD License)

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1\. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2\. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3\. Neither the names of the copyright holders nor the names of the contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

This software is provided by the copyright holders and contributors "as is" and
any express or implied warranties, including, but not limited to, the implied
warranties of merchantability and fitness for a particular purpose are disclaimed.
In no event shall copyright holders or contributors be liable for any direct,
indirect, incidental, special, exemplary, or consequential damages (including,
but not limited to, procurement of substitute goods or services; loss of use, data,
or profits; or business interruption) however caused and on any theory of liability,
whether in contract, strict liability, or tort (including negligence or otherwise)
arising in any way out of the use of this software, even if advised of the
possibility of such damage.

## <a id="ompl"></a>License of the Open Motion Planning Library

BSD License

Copyright (c) 2010–2018, Rice University. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. Neither the name of the Rice University nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## <a id="reflexxes"></a>License of the Reflexxes Motion Library (RML) Type II

The Reflexxes Motion Library Type II is licensed under [LGPL V3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)

## <a id="ruckig"></a>License of the Ruckig Online Trajectory Generation library

MIT License

Copyright (c) 2021 Lars Berscheid

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="toppra"></a>License of the TOPP-RA library

The TOPP-RA library is licensed under the MIT License:

Copyright (c) 2017 Hung Pham

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="replxx"></a>License of the Replxx library

Copyright (c) 2017-2018, Marcin Konarski (amok at codestation.org)

Copyright (c) 2010, Salvatore Sanfilippo (antirez at gmail dot com)

Copyright (c) 2010, Pieter Noordhuis (pcnoordhuis at gmail dot com)

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of Redis nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

wcwidth.cpp

Markus Kuhn -- 2007-05-26 (Unicode 5.0)

Permission to use, copy, modify, and distribute this software for any purpose and without fee is hereby granted. The author disclaims all warranties with regard to this software.

ConvertUTF.cpp

Copyright 2001-2004 Unicode, Inc.

Disclaimer

This source code is provided as is by Unicode, Inc. No claims are made as to fitness for any particular purpose. No warranties of any kind are expressed or implied. The recipient agrees to determine applicability of information provided. If this file has been purchased on magnetic or optical media from Unicode, Inc., the sole remedy for any claim will be exchange of defective media within 90 days of receipt.

Limitations on Rights to Redistribute This Code

Unicode, Inc. hereby grants the right to freely use the information supplied in this file in the creation of products supporting the Unicode Standard, and to make copies of this file in any form for internal or external distribution as long as this notice remains attached.

## <a id="replxx-2"></a>License of the sha1 lua module

Copyright (c) 2013 Enrique García Cota, Eike Decker, Jeffrey Friedl
Copyright (c) 2018 Peter Melnichenko

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## <a id="middleclass"></a>License of the middleclass lua library

Copyright (c) 2011 Enrique García Cota

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
