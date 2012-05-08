import matplotlib
matplotlib.use('Agg')
import pylab as plt

import lsst.afw.detection as afwDet
import lsst.afw.image as afwImg
import lsst.meas.deblender as measDeblend

def main():
    butils = measDeblend.BaselineUtilsF
    foot = buildExample()

    fbb = foot.getBBox()
    mask1 = afwImg.MaskU(fbb.getWidth(), fbb.getHeight())
    mask1.setXY0(fbb.getMinX(), fbb.getMinY())
    afwDet.setMaskFromFootprint(mask1, foot, 1)

    plt.clf()
    plt.imshow(mask1.getArray(), origin='lower', interpolation='nearest',
               extent=(fbb.getMinX(), fbb.getMaxX(), fbb.getMinY(), fbb.getMaxY()))
    plt.gray()
    plt.savefig('foot.png')

    sfoot = butils.symmetrizeFootprint(foot, 355, 227)

    mask2 = afwImg.MaskU(fbb.getWidth(), fbb.getHeight())
    mask2.setXY0(fbb.getMinX(), fbb.getMinY())
    afwDet.setMaskFromFootprint(mask2, sfoot, 1)
    
    plt.clf()
    plt.imshow(mask2.getArray(), origin='lower', interpolation='nearest',
               extent=(fbb.getMinX(), fbb.getMaxX(), fbb.getMinY(), fbb.getMaxY()))
    plt.gray()
    plt.savefig('sfoot.png')

    plt.plot([364], [111], 'r.')
    plt.plot([367], [117], 'r.')
    plt.savefig('sfoot2.png')


    foot = buildExample2()

    fbb = foot.getBBox()
    mask1 = afwImg.MaskU(fbb.getWidth(), fbb.getHeight())
    mask1.setXY0(fbb.getMinX(), fbb.getMinY())
    afwDet.setMaskFromFootprint(mask1, foot, 1)

    plt.clf()
    plt.imshow(mask1.getArray(), origin='lower', interpolation='nearest',
               extent=(fbb.getMinX(), fbb.getMaxX(), fbb.getMinY(), fbb.getMaxY()))
    plt.gray()
    plt.savefig('foot2.png')

    sfoot = butils.symmetrizeFootprint(foot, 355, 227)

    mask2 = afwImg.MaskU(fbb.getWidth(), fbb.getHeight())
    mask2.setXY0(fbb.getMinX(), fbb.getMinY())
    afwDet.setMaskFromFootprint(mask2, sfoot, 1)
    
    plt.clf()
    plt.imshow(mask2.getArray(), origin='lower', interpolation='nearest',
               extent=(fbb.getMinX(), fbb.getMaxX(), fbb.getMinY(), fbb.getMaxY()))
    plt.gray()
    plt.savefig('sfoot3.png')

    #plt.plot([364], [111], 'r.')
    #plt.plot([367], [117], 'r.')
    #plt.savefig('sfoot4.png')




def buildExample():
    foot = afwDet.Footprint()
    foot.addSpan(12, 275, 432)
    foot.addSpan(13, 274, 440)
    foot.addSpan(14, 272, 443)
    foot.addSpan(15, 271, 444)
    foot.addSpan(16, 271, 444)
    foot.addSpan(17, 270, 444)
    foot.addSpan(18, 270, 444)
    foot.addSpan(19, 270, 445)
    foot.addSpan(20, 270, 436)
    foot.addSpan(20, 438, 445)
    foot.addSpan(21, 271, 434)
    foot.addSpan(21, 440, 445)
    foot.addSpan(22, 271, 433)
    foot.addSpan(23, 272, 434)
    foot.addSpan(24, 272, 435)
    foot.addSpan(25, 273, 436)
    foot.addSpan(26, 273, 437)
    foot.addSpan(27, 272, 438)
    foot.addSpan(28, 271, 439)
    foot.addSpan(29, 271, 440)
    foot.addSpan(30, 271, 440)
    foot.addSpan(31, 272, 440)
    foot.addSpan(32, 272, 441)
    foot.addSpan(33, 272, 441)
    foot.addSpan(34, 272, 441)
    foot.addSpan(35, 273, 441)
    foot.addSpan(36, 274, 440)
    foot.addSpan(37, 275, 440)
    foot.addSpan(38, 275, 440)
    foot.addSpan(39, 275, 440)
    foot.addSpan(40, 274, 440)
    foot.addSpan(41, 273, 440)
    foot.addSpan(42, 271, 435)
    foot.addSpan(42, 438, 440)
    foot.addSpan(43, 270, 434)
    foot.addSpan(44, 269, 433)
    foot.addSpan(45, 269, 432)
    foot.addSpan(46, 268, 432)
    foot.addSpan(47, 268, 431)
    foot.addSpan(48, 267, 430)
    foot.addSpan(49, 267, 430)
    foot.addSpan(50, 267, 430)
    foot.addSpan(51, 266, 431)
    foot.addSpan(52, 266, 432)
    foot.addSpan(53, 266, 432)
    foot.addSpan(54, 266, 432)
    foot.addSpan(55, 266, 432)
    foot.addSpan(56, 268, 433)
    foot.addSpan(57, 269, 433)
    foot.addSpan(58, 270, 434)
    foot.addSpan(59, 271, 434)
    foot.addSpan(60, 272, 434)
    foot.addSpan(61, 273, 434)
    foot.addSpan(62, 275, 433)
    foot.addSpan(63, 280, 433)
    foot.addSpan(64, 280, 432)
    foot.addSpan(65, 280, 431)
    foot.addSpan(66, 280, 430)
    foot.addSpan(67, 279, 422)
    foot.addSpan(67, 424, 430)
    foot.addSpan(68, 278, 421)
    foot.addSpan(68, 427, 429)
    foot.addSpan(69, 277, 421)
    foot.addSpan(70, 277, 421)
    foot.addSpan(71, 277, 421)
    foot.addSpan(72, 277, 421)
    foot.addSpan(73, 278, 421)
    foot.addSpan(74, 278, 421)
    foot.addSpan(75, 278, 419)
    foot.addSpan(76, 278, 416)
    foot.addSpan(77, 278, 285)
    foot.addSpan(77, 288, 416)
    foot.addSpan(78, 290, 416)
    foot.addSpan(79, 297, 416)
    foot.addSpan(80, 298, 418)
    foot.addSpan(81, 299, 419)
    foot.addSpan(82, 300, 419)
    foot.addSpan(83, 301, 419)
    foot.addSpan(84, 301, 417)
    foot.addSpan(85, 301, 416)
    foot.addSpan(86, 301, 415)
    foot.addSpan(87, 301, 415)
    foot.addSpan(88, 301, 415)
    foot.addSpan(89, 302, 414)
    foot.addSpan(90, 302, 413)
    foot.addSpan(91, 302, 412)
    foot.addSpan(92, 302, 400)
    foot.addSpan(92, 403, 408)
    foot.addSpan(93, 304, 313)
    foot.addSpan(93, 315, 400)
    foot.addSpan(94, 306, 312)
    foot.addSpan(94, 316, 400)
    foot.addSpan(95, 307, 311)
    foot.addSpan(95, 317, 400)
    foot.addSpan(96, 308, 312)
    foot.addSpan(96, 318, 400)
    foot.addSpan(97, 308, 312)
    foot.addSpan(97, 318, 400)
    foot.addSpan(98, 309, 313)
    foot.addSpan(98, 319, 399)
    foot.addSpan(99, 309, 313)
    foot.addSpan(99, 321, 399)
    foot.addSpan(100, 310, 313)
    foot.addSpan(100, 323, 398)
    foot.addSpan(101, 311, 312)
    foot.addSpan(101, 323, 398)
    foot.addSpan(102, 323, 398)
    foot.addSpan(103, 323, 398)
    foot.addSpan(104, 322, 398)
    foot.addSpan(105, 322, 398)
    foot.addSpan(106, 323, 398)
    foot.addSpan(107, 323, 399)
    foot.addSpan(108, 323, 400)
    foot.addSpan(109, 324, 372)
    foot.addSpan(109, 375, 401)
    foot.addSpan(110, 324, 372)
    foot.addSpan(110, 375, 401)
    foot.addSpan(111, 325, 372)
    foot.addSpan(111, 375, 397)
    foot.addSpan(111, 400, 401)
    foot.addSpan(112, 325, 394)
    foot.addSpan(112, 401, 401)
    foot.addSpan(113, 326, 394)
    foot.addSpan(114, 325, 396)
    foot.addSpan(115, 323, 396)
    foot.addSpan(116, 323, 390)
    foot.addSpan(116, 392, 396)
    foot.addSpan(117, 323, 328)
    foot.addSpan(117, 335, 370)
    foot.addSpan(117, 378, 387)
    foot.addSpan(117, 393, 396)
    foot.addSpan(118, 323, 327)
    foot.addSpan(118, 338, 369)
    foot.addSpan(118, 379, 386)
    foot.addSpan(118, 393, 396)
    foot.addSpan(119, 323, 327)
    foot.addSpan(119, 340, 369)
    foot.addSpan(119, 380, 386)
    foot.addSpan(119, 394, 396)
    foot.addSpan(120, 324, 326)
    foot.addSpan(120, 342, 369)
    foot.addSpan(120, 380, 386)
    foot.addSpan(120, 394, 396)
    foot.addSpan(121, 324, 325)
    foot.addSpan(121, 343, 369)
    foot.addSpan(121, 381, 385)
    foot.addSpan(121, 395, 396)
    foot.addSpan(122, 323, 324)
    foot.addSpan(122, 343, 368)
    foot.addSpan(122, 382, 385)
    foot.addSpan(122, 395, 396)
    foot.addSpan(123, 322, 324)
    foot.addSpan(123, 343, 368)
    foot.addSpan(123, 382, 384)
    foot.addSpan(123, 395, 396)
    foot.addSpan(124, 322, 324)
    foot.addSpan(124, 343, 368)
    foot.addSpan(125, 322, 324)
    foot.addSpan(125, 343, 368)
    foot.addSpan(126, 323, 323)
    foot.addSpan(126, 343, 368)
    foot.addSpan(127, 343, 368)
    foot.addSpan(128, 343, 368)
    foot.addSpan(129, 343, 367)
    foot.addSpan(130, 343, 367)
    foot.addSpan(131, 343, 367)
    foot.addSpan(132, 343, 367)
    foot.addSpan(133, 343, 367)
    foot.addSpan(134, 343, 367)
    foot.addSpan(135, 344, 367)
    foot.addSpan(136, 344, 367)
    foot.addSpan(137, 344, 367)
    foot.addSpan(138, 344, 367)
    foot.addSpan(139, 344, 367)
    foot.addSpan(140, 344, 367)
    foot.addSpan(141, 344, 367)
    foot.addSpan(142, 344, 367)
    foot.addSpan(143, 344, 367)
    foot.addSpan(144, 344, 367)
    foot.addSpan(145, 344, 367)
    foot.addSpan(146, 344, 367)
    foot.addSpan(147, 344, 367)
    foot.addSpan(148, 344, 367)
    foot.addSpan(149, 344, 367)
    foot.addSpan(150, 344, 367)
    foot.addSpan(151, 344, 367)
    foot.addSpan(152, 345, 367)
    foot.addSpan(153, 345, 367)
    foot.addSpan(154, 345, 367)
    foot.addSpan(155, 345, 367)
    foot.addSpan(156, 345, 367)
    foot.addSpan(157, 345, 367)
    foot.addSpan(158, 345, 367)
    foot.addSpan(159, 345, 367)
    foot.addSpan(160, 345, 367)
    foot.addSpan(161, 345, 367)
    foot.addSpan(162, 345, 367)
    foot.addSpan(163, 345, 367)
    foot.addSpan(164, 345, 367)
    foot.addSpan(165, 345, 367)
    foot.addSpan(166, 345, 367)
    foot.addSpan(167, 345, 367)
    foot.addSpan(168, 345, 367)
    foot.addSpan(169, 345, 367)
    foot.addSpan(170, 345, 367)
    foot.addSpan(171, 345, 367)
    foot.addSpan(172, 345, 367)
    foot.addSpan(173, 345, 367)
    foot.addSpan(174, 345, 367)
    foot.addSpan(175, 345, 367)
    foot.addSpan(176, 345, 367)
    foot.addSpan(177, 345, 367)
    foot.addSpan(178, 345, 367)
    foot.addSpan(179, 345, 367)
    foot.addSpan(180, 345, 367)
    foot.addSpan(181, 345, 367)
    foot.addSpan(182, 345, 367)
    foot.addSpan(183, 345, 367)
    foot.addSpan(184, 345, 367)
    foot.addSpan(185, 345, 367)
    foot.addSpan(186, 345, 367)
    foot.addSpan(187, 345, 367)
    foot.addSpan(188, 345, 367)
    foot.addSpan(189, 345, 367)
    foot.addSpan(190, 345, 367)
    foot.addSpan(191, 345, 367)
    foot.addSpan(192, 345, 367)
    foot.addSpan(193, 345, 367)
    foot.addSpan(194, 345, 367)
    foot.addSpan(195, 345, 367)
    foot.addSpan(196, 345, 367)
    foot.addSpan(197, 345, 367)
    foot.addSpan(198, 345, 367)
    foot.addSpan(199, 345, 367)
    foot.addSpan(200, 345, 367)
    foot.addSpan(201, 345, 366)
    foot.addSpan(202, 345, 366)
    foot.addSpan(203, 345, 366)
    foot.addSpan(204, 345, 366)
    foot.addSpan(205, 345, 366)
    foot.addSpan(206, 345, 366)
    foot.addSpan(207, 345, 366)
    foot.addSpan(208, 345, 366)
    foot.addSpan(209, 345, 366)
    foot.addSpan(210, 344, 366)
    foot.addSpan(211, 344, 366)
    foot.addSpan(212, 344, 366)
    foot.addSpan(213, 344, 366)
    foot.addSpan(214, 345, 366)
    foot.addSpan(215, 345, 366)
    foot.addSpan(216, 345, 366)
    foot.addSpan(217, 345, 366)
    foot.addSpan(218, 345, 366)
    foot.addSpan(219, 345, 366)
    foot.addSpan(220, 345, 366)
    foot.addSpan(221, 345, 366)
    foot.addSpan(222, 345, 366)
    foot.addSpan(223, 345, 366)
    foot.addSpan(224, 345, 365)
    foot.addSpan(225, 345, 365)
    foot.addSpan(226, 345, 365)
    foot.addSpan(227, 345, 365)
    foot.addSpan(228, 345, 365)
    foot.addSpan(229, 345, 366)
    foot.addSpan(230, 345, 366)
    foot.addSpan(231, 345, 366)
    foot.addSpan(232, 345, 366)
    foot.addSpan(233, 345, 366)
    foot.addSpan(234, 345, 366)
    foot.addSpan(235, 345, 366)
    foot.addSpan(236, 345, 366)
    foot.addSpan(237, 345, 365)
    foot.addSpan(238, 345, 365)
    foot.addSpan(239, 345, 365)
    foot.addSpan(240, 345, 366)
    foot.addSpan(241, 345, 366)
    foot.addSpan(242, 345, 365)
    foot.addSpan(243, 345, 365)
    foot.addSpan(244, 345, 365)
    foot.addSpan(245, 345, 365)
    foot.addSpan(246, 345, 365)
    foot.addSpan(247, 345, 365)
    foot.addSpan(248, 345, 365)
    foot.addSpan(249, 345, 365)
    foot.addSpan(250, 338, 341)
    foot.addSpan(250, 345, 365)
    foot.addSpan(251, 337, 343)
    foot.addSpan(251, 345, 365)
    foot.addSpan(252, 336, 365)
    foot.addSpan(253, 336, 365)
    foot.addSpan(254, 337, 365)
    foot.addSpan(255, 337, 366)
    foot.addSpan(256, 337, 366)
    foot.addSpan(257, 337, 365)
    foot.addSpan(258, 337, 365)
    foot.addSpan(259, 338, 365)
    foot.addSpan(260, 338, 365)
    foot.addSpan(261, 339, 365)
    foot.addSpan(262, 339, 365)
    foot.addSpan(263, 341, 365)
    foot.addSpan(264, 346, 365)
    foot.addSpan(265, 346, 365)
    foot.addSpan(266, 346, 365)
    foot.addSpan(267, 346, 365)
    foot.addSpan(268, 346, 365)
    foot.addSpan(269, 346, 365)
    foot.addSpan(270, 346, 365)
    foot.addSpan(271, 346, 365)
    foot.addSpan(272, 346, 365)
    foot.addSpan(273, 346, 365)
    foot.addSpan(274, 346, 365)
    foot.addSpan(275, 346, 365)
    foot.addSpan(276, 346, 365)
    foot.addSpan(277, 346, 365)
    foot.addSpan(278, 346, 365)
    foot.addSpan(279, 346, 365)
    foot.addSpan(280, 346, 365)
    foot.addSpan(281, 346, 365)
    foot.addSpan(282, 346, 365)
    foot.addSpan(283, 346, 365)
    foot.addSpan(284, 345, 365)
    foot.addSpan(285, 342, 365)
    foot.addSpan(286, 342, 365)
    foot.addSpan(287, 341, 365)
    foot.addSpan(288, 341, 365)
    foot.addSpan(289, 340, 365)
    foot.addSpan(290, 340, 365)
    foot.addSpan(291, 339, 365)
    foot.addSpan(292, 335, 365)
    foot.addSpan(293, 334, 365)
    foot.addSpan(294, 333, 365)
    foot.addSpan(295, 333, 342)
    foot.addSpan(295, 346, 366)
    foot.addSpan(296, 333, 341)
    foot.addSpan(296, 346, 366)
    foot.addSpan(297, 333, 339)
    foot.addSpan(297, 346, 366)
    foot.addSpan(298, 333, 338)
    foot.addSpan(298, 346, 366)
    foot.addSpan(299, 346, 368)
    foot.addSpan(300, 346, 370)
    foot.addSpan(301, 346, 371)
    foot.addSpan(302, 346, 372)
    foot.addSpan(303, 346, 373)
    foot.addSpan(304, 346, 374)
    foot.addSpan(305, 346, 374)
    foot.addSpan(306, 346, 375)
    foot.addSpan(307, 346, 375)
    foot.addSpan(308, 346, 375)
    foot.addSpan(309, 345, 375)
    foot.addSpan(310, 345, 375)
    foot.addSpan(311, 345, 376)
    foot.addSpan(312, 344, 376)
    foot.addSpan(313, 344, 376)
    foot.addSpan(314, 344, 376)
    foot.addSpan(315, 344, 376)
    foot.addSpan(316, 343, 376)
    foot.addSpan(317, 343, 375)
    foot.addSpan(318, 342, 375)
    foot.addSpan(319, 341, 374)
    foot.addSpan(320, 341, 373)
    foot.addSpan(321, 341, 373)
    foot.addSpan(322, 341, 372)
    foot.addSpan(323, 341, 372)
    foot.addSpan(324, 341, 371)
    foot.addSpan(325, 341, 371)
    foot.addSpan(326, 341, 370)
    foot.addSpan(327, 342, 370)
    foot.addSpan(328, 342, 369)
    foot.addSpan(329, 342, 369)
    foot.addSpan(330, 342, 367)
    foot.addSpan(331, 343, 367)
    foot.addSpan(332, 343, 366)
    foot.addSpan(333, 343, 366)
    foot.addSpan(334, 342, 366)
    foot.addSpan(335, 342, 366)
    foot.addSpan(336, 342, 366)
    foot.addSpan(337, 342, 366)
    foot.addSpan(338, 342, 366)
    foot.addSpan(339, 343, 366)
    foot.addSpan(340, 344, 366)
    foot.addSpan(341, 345, 365)
    foot.addSpan(342, 346, 365)
    foot.addSpan(343, 346, 365)
    foot.addSpan(344, 346, 365)
    foot.addSpan(345, 346, 365)
    foot.addSpan(346, 346, 365)
    foot.addSpan(347, 346, 365)
    foot.addSpan(348, 346, 366)
    foot.addSpan(349, 346, 366)
    foot.addSpan(350, 346, 366)
    foot.addSpan(351, 346, 365)
    foot.addSpan(352, 346, 365)
    foot.addSpan(353, 346, 365)
    foot.addSpan(354, 346, 365)
    foot.addSpan(355, 346, 365)
    foot.addSpan(356, 346, 365)
    foot.addSpan(357, 346, 365)
    foot.addSpan(358, 346, 365)
    foot.addSpan(359, 346, 365)
    foot.addSpan(360, 346, 365)
    foot.addSpan(361, 346, 365)
    foot.addSpan(362, 346, 365)
    foot.addSpan(363, 346, 365)
    foot.addSpan(364, 346, 365)
    foot.addSpan(365, 346, 365)
    foot.addSpan(366, 346, 365)
    foot.addSpan(367, 340, 340)
    foot.addSpan(367, 345, 365)
    foot.addSpan(368, 338, 343)
    foot.addSpan(368, 345, 365)
    foot.addSpan(369, 337, 365)
    foot.addSpan(370, 337, 365)
    foot.addSpan(371, 337, 365)
    foot.addSpan(372, 337, 365)
    foot.addSpan(373, 337, 365)
    foot.addSpan(374, 337, 365)
    foot.addSpan(375, 337, 365)
    foot.addSpan(376, 337, 365)
    foot.addSpan(377, 337, 365)
    foot.addSpan(378, 337, 365)
    foot.addSpan(379, 337, 365)
    foot.addSpan(380, 337, 365)
    foot.addSpan(381, 338, 365)
    foot.addSpan(382, 346, 365)
    foot.addSpan(383, 346, 365)
    foot.addSpan(384, 346, 364)
    foot.addSpan(385, 346, 364)
    foot.addSpan(386, 346, 364)
    foot.addSpan(387, 346, 364)
    foot.addSpan(388, 346, 364)
    foot.addSpan(389, 346, 364)
    foot.addSpan(390, 346, 364)
    foot.addSpan(391, 346, 364)
    foot.addSpan(392, 346, 364)
    foot.addSpan(393, 346, 364)
    foot.addSpan(394, 346, 364)
    foot.addSpan(395, 346, 364)
    foot.addSpan(396, 346, 364)
    foot.addSpan(397, 346, 364)
    foot.addSpan(398, 346, 364)
    foot.addSpan(399, 346, 364)
    foot.addSpan(400, 346, 364)
    foot.addSpan(401, 346, 364)
    foot.addSpan(402, 346, 364)
    foot.addSpan(403, 346, 364)
    foot.addSpan(404, 346, 364)
    foot.addSpan(405, 346, 364)
    foot.addSpan(406, 346, 364)
    foot.addSpan(407, 346, 364)
    foot.addSpan(408, 346, 364)
    foot.addSpan(409, 346, 364)
    foot.addSpan(410, 346, 364)
    foot.addSpan(411, 346, 364)
    foot.addSpan(412, 346, 364)
    foot.addSpan(413, 346, 364)
    foot.addSpan(414, 346, 364)
    foot.addSpan(415, 346, 364)
    foot.addSpan(416, 346, 364)
    foot.addSpan(417, 346, 364)
    foot.addSpan(418, 346, 364)
    foot.addSpan(419, 346, 364)
    foot.addSpan(420, 346, 364)
    foot.addSpan(421, 346, 364)
    foot.addSpan(422, 346, 364)
    foot.addSpan(423, 346, 364)
    foot.addSpan(424, 346, 364)
    foot.addSpan(425, 346, 364)
    foot.addSpan(426, 345, 364)
    foot.addSpan(427, 344, 364)
    foot.addSpan(428, 343, 364)
    foot.addSpan(429, 343, 364)
    foot.addSpan(430, 342, 364)
    foot.addSpan(431, 342, 364)
    foot.addSpan(432, 342, 364)
    foot.addSpan(433, 342, 364)
    foot.addSpan(434, 343, 364)
    foot.addSpan(435, 343, 364)
    foot.addSpan(436, 345, 364)
    foot.addSpan(437, 346, 364)
    foot.addSpan(438, 347, 364)
    foot.addSpan(439, 347, 364)
    foot.addSpan(440, 347, 364)
    foot.addSpan(441, 347, 364)
    foot.addSpan(441, 393, 393)
    foot.addSpan(442, 347, 364)
    foot.addSpan(442, 389, 397)
    foot.addSpan(443, 347, 364)
    foot.addSpan(443, 382, 401)
    foot.addSpan(444, 347, 364)
    foot.addSpan(444, 379, 403)
    foot.addSpan(445, 347, 364)
    foot.addSpan(445, 377, 405)
    foot.addSpan(446, 347, 364)
    foot.addSpan(446, 376, 406)
    foot.addSpan(447, 347, 364)
    foot.addSpan(447, 375, 407)
    foot.addSpan(448, 347, 364)
    foot.addSpan(448, 374, 408)
    foot.addSpan(449, 347, 364)
    foot.addSpan(449, 371, 408)
    foot.addSpan(450, 347, 364)
    foot.addSpan(450, 369, 409)
    foot.addSpan(451, 347, 364)
    foot.addSpan(451, 369, 410)
    foot.addSpan(452, 347, 365)
    foot.addSpan(452, 368, 411)
    foot.addSpan(453, 347, 365)
    foot.addSpan(453, 367, 411)
    foot.addSpan(454, 347, 412)
    foot.addSpan(455, 347, 411)
    foot.addSpan(456, 347, 411)
    foot.addSpan(457, 347, 409)
    foot.addSpan(458, 347, 408)
    foot.addSpan(459, 347, 408)
    foot.addSpan(460, 347, 407)
    foot.addSpan(461, 347, 407)
    foot.addSpan(462, 347, 406)
    foot.addSpan(463, 347, 405)
    foot.addSpan(464, 347, 405)
    foot.addSpan(465, 347, 404)
    foot.addSpan(466, 347, 404)
    foot.addSpan(467, 347, 404)
    foot.addSpan(468, 347, 403)
    foot.addSpan(469, 347, 402)
    foot.addSpan(470, 347, 402)
    foot.addSpan(471, 347, 401)
    foot.addSpan(472, 347, 401)
    foot.addSpan(473, 347, 400)
    foot.addSpan(474, 347, 400)
    foot.addSpan(475, 347, 396)
    foot.addSpan(476, 347, 392)
    foot.addSpan(477, 347, 389)
    foot.addSpan(478, 347, 365)
    foot.addSpan(478, 372, 381)
    foot.addSpan(479, 347, 364)
    foot.addSpan(480, 347, 364)
    foot.addSpan(481, 347, 364)
    foot.addSpan(482, 347, 364)
    foot.addSpan(483, 347, 364)
    foot.addSpan(484, 347, 364)
    foot.addSpan(485, 347, 364)
    foot.addSpan(486, 347, 364)
    foot.addSpan(487, 347, 364)
    foot.addSpan(488, 347, 364)
    foot.addSpan(489, 347, 364)
    foot.addSpan(490, 347, 364)
    foot.addSpan(491, 347, 364)
    foot.addSpan(492, 347, 364)
    foot.addSpan(493, 347, 364)
    foot.addSpan(494, 347, 364)
    foot.addSpan(495, 347, 364)
    foot.addSpan(496, 347, 364)
    foot.addSpan(497, 347, 364)
    foot.addSpan(498, 347, 364)
    foot.addSpan(499, 347, 364)
    foot.addSpan(500, 347, 364)
    foot.addSpan(501, 347, 364)
    foot.addSpan(502, 347, 364)
    foot.addSpan(503, 347, 364)
    foot.addSpan(504, 347, 364)
    foot.addSpan(505, 347, 364)
    foot.addSpan(506, 338, 342)
    foot.addSpan(506, 346, 364)
    foot.addSpan(507, 337, 343)
    foot.addSpan(507, 345, 364)
    foot.addSpan(508, 335, 364)
    foot.addSpan(509, 334, 364)
    foot.addSpan(510, 333, 364)
    foot.addSpan(511, 333, 365)
    foot.addSpan(512, 331, 365)
    foot.addSpan(513, 320, 323)
    foot.addSpan(513, 330, 365)
    foot.addSpan(514, 319, 365)
    foot.addSpan(515, 318, 365)
    foot.addSpan(516, 317, 365)
    foot.addSpan(517, 317, 365)
    foot.addSpan(518, 317, 365)
    foot.addSpan(519, 317, 365)
    foot.addSpan(520, 317, 366)
    foot.addSpan(521, 316, 367)
    foot.addSpan(522, 315, 367)
    foot.addSpan(523, 313, 368)
    foot.addSpan(524, 311, 368)
    foot.addSpan(525, 310, 369)
    foot.addSpan(526, 309, 369)
    foot.addSpan(527, 309, 368)
    foot.addSpan(528, 309, 369)
    foot.addSpan(529, 309, 370)
    foot.addSpan(530, 310, 374)
    foot.addSpan(531, 310, 375)
    foot.addSpan(532, 311, 374)
    foot.addSpan(533, 311, 373)
    foot.addSpan(534, 311, 372)
    foot.addSpan(535, 311, 372)
    foot.addSpan(536, 312, 372)
    foot.addSpan(537, 312, 373)
    foot.addSpan(538, 312, 373)
    foot.addSpan(539, 311, 374)
    foot.addSpan(540, 310, 374)
    foot.addSpan(541, 310, 375)
    foot.addSpan(542, 310, 375)
    foot.addSpan(543, 310, 375)
    foot.addSpan(544, 310, 375)
    foot.addSpan(545, 311, 375)
    foot.addSpan(546, 312, 374)
    foot.addSpan(547, 312, 374)
    foot.addSpan(548, 313, 373)
    foot.addSpan(549, 313, 372)
    foot.addSpan(550, 313, 370)
    foot.addSpan(551, 313, 369)
    foot.addSpan(552, 313, 369)
    foot.addSpan(553, 313, 369)
    foot.addSpan(554, 314, 369)
    foot.addSpan(555, 314, 369)
    foot.addSpan(556, 316, 369)
    foot.addSpan(557, 318, 368)
    foot.addSpan(558, 319, 368)
    foot.addSpan(559, 319, 368)
    foot.addSpan(560, 319, 366)
    foot.addSpan(560, 369, 371)
    foot.addSpan(561, 319, 365)
    foot.addSpan(561, 369, 371)
    foot.addSpan(562, 319, 365)
    foot.addSpan(562, 369, 371)
    foot.addSpan(563, 319, 365)
    foot.addSpan(563, 370, 370)
    foot.addSpan(564, 320, 365)
    foot.addSpan(565, 323, 364)
    foot.addSpan(566, 324, 364)
    foot.addSpan(567, 325, 364)
    foot.addSpan(568, 325, 364)
    foot.addSpan(569, 324, 339)
    foot.addSpan(569, 345, 364)
    foot.addSpan(570, 323, 337)
    foot.addSpan(570, 345, 364)
    foot.addSpan(571, 320, 336)
    foot.addSpan(571, 346, 368)
    foot.addSpan(572, 318, 335)
    foot.addSpan(572, 346, 369)
    foot.addSpan(573, 318, 334)
    foot.addSpan(573, 346, 370)
    foot.addSpan(574, 317, 334)
    foot.addSpan(574, 346, 370)
    foot.addSpan(575, 317, 335)
    foot.addSpan(575, 346, 363)
    foot.addSpan(575, 367, 369)
    foot.addSpan(576, 317, 335)
    foot.addSpan(576, 346, 363)
    foot.addSpan(576, 368, 368)
    foot.addSpan(577, 317, 335)
    foot.addSpan(577, 346, 363)
    foot.addSpan(578, 317, 335)
    foot.addSpan(578, 346, 363)
    foot.addSpan(579, 317, 335)
    foot.addSpan(579, 346, 363)
    foot.addSpan(580, 317, 335)
    foot.addSpan(580, 346, 363)
    foot.addSpan(581, 318, 335)
    foot.addSpan(581, 347, 363)
    foot.addSpan(582, 318, 334)
    foot.addSpan(582, 347, 363)
    foot.addSpan(583, 319, 334)
    foot.addSpan(583, 347, 363)
    foot.addSpan(584, 319, 333)
    foot.addSpan(584, 347, 363)
    foot.addSpan(585, 320, 332)
    foot.addSpan(585, 347, 363)
    foot.addSpan(586, 321, 331)
    foot.addSpan(586, 347, 363)
    foot.addSpan(587, 322, 327)
    foot.addSpan(587, 347, 363)
    foot.addSpan(588, 347, 363)
    foot.addSpan(589, 347, 363)
    foot.addSpan(590, 348, 362)
    foot.addSpan(591, 348, 362)
    foot.addSpan(592, 348, 361)
    foot.addSpan(593, 349, 360)
    foot.addSpan(594, 350, 359)
    foot.addSpan(595, 351, 358)
    foot.addSpan(596, 353, 355)
    foot.normalize()
    return foot

def buildExample2():
    foot = afwDet.Footprint()
    foot.addSpan(110, 324, 372)
    foot.addSpan(110, 375, 401)
    foot.addSpan(111, 325, 372)
    foot.addSpan(111, 375, 397)
    foot.addSpan(111, 400, 401)
    foot.addSpan(112, 325, 394)
    foot.addSpan(112, 401, 401)
    foot.addSpan(113, 326, 394)
    foot.addSpan(114, 325, 396)
    foot.addSpan(115, 323, 396)
    foot.addSpan(116, 323, 390)
    foot.addSpan(116, 392, 396)
    foot.addSpan(117, 323, 328)
    foot.addSpan(117, 335, 370)
    foot.addSpan(117, 378, 387)
    foot.addSpan(117, 393, 396)
    foot.addSpan(118, 323, 327)
    foot.addSpan(118, 338, 369)
    foot.addSpan(118, 379, 386)
    foot.addSpan(118, 393, 396)
    foot.addSpan(119, 323, 327)
    foot.addSpan(119, 340, 369)
    foot.addSpan(119, 380, 386)
    foot.addSpan(119, 394, 396)
    foot.addSpan(120, 324, 326)
    foot.addSpan(120, 342, 369)
    foot.addSpan(120, 380, 386)
    foot.addSpan(120, 394, 396)
    foot.addSpan(121, 324, 325)
    foot.addSpan(121, 343, 369)
    foot.addSpan(121, 381, 385)
    foot.addSpan(121, 395, 396)
    foot.addSpan(122, 323, 324)
    foot.addSpan(122, 343, 368)
    foot.addSpan(122, 382, 385)
    foot.addSpan(122, 395, 396)
    foot.addSpan(123, 322, 324)
    foot.addSpan(123, 343, 368)
    foot.addSpan(123, 382, 384)
    foot.addSpan(123, 395, 396)
    foot.addSpan(124, 322, 324)
    foot.addSpan(124, 343, 368)
    foot.addSpan(125, 322, 324)
    foot.addSpan(125, 343, 368)
    foot.addSpan(126, 323, 323)
    foot.addSpan(126, 343, 368)
    foot.addSpan(127, 343, 368)
    foot.addSpan(128, 343, 368)
    foot.addSpan(129, 343, 367)
    foot.addSpan(130, 343, 367)
    foot.addSpan(131, 343, 367)
    foot.addSpan(132, 343, 367)
    foot.addSpan(133, 343, 367)
    foot.addSpan(134, 343, 367)
    foot.addSpan(135, 344, 367)
    foot.addSpan(136, 344, 367)
    foot.addSpan(137, 344, 367)
    foot.addSpan(138, 344, 367)
    foot.addSpan(139, 344, 367)
    foot.addSpan(140, 344, 367)
    foot.addSpan(141, 344, 367)
    foot.addSpan(142, 344, 367)
    foot.addSpan(143, 344, 367)
    foot.addSpan(144, 344, 367)
    foot.addSpan(145, 344, 367)
    foot.addSpan(146, 344, 367)
    foot.addSpan(147, 344, 367)
    foot.addSpan(148, 344, 367)
    foot.addSpan(149, 344, 367)
    foot.addSpan(150, 344, 367)
    foot.addSpan(151, 344, 367)
    foot.addSpan(152, 345, 367)
    foot.addSpan(153, 345, 367)
    foot.addSpan(154, 345, 367)
    foot.addSpan(155, 345, 367)
    foot.addSpan(156, 345, 367)
    foot.addSpan(157, 345, 367)
    foot.addSpan(158, 345, 367)
    foot.addSpan(159, 345, 367)
    foot.addSpan(160, 345, 367)
    foot.addSpan(161, 345, 367)
    foot.addSpan(162, 345, 367)
    foot.addSpan(163, 345, 367)
    foot.addSpan(164, 345, 367)
    foot.addSpan(165, 345, 367)
    foot.addSpan(166, 345, 367)
    foot.addSpan(167, 345, 367)
    foot.addSpan(168, 345, 367)
    foot.addSpan(169, 345, 367)
    foot.addSpan(170, 345, 367)
    foot.addSpan(171, 345, 367)
    foot.addSpan(172, 345, 367)
    foot.addSpan(173, 345, 367)
    foot.addSpan(174, 345, 367)
    foot.addSpan(175, 345, 367)
    foot.addSpan(176, 345, 367)
    foot.addSpan(177, 345, 367)
    foot.addSpan(178, 345, 367)
    foot.addSpan(179, 345, 367)
    foot.addSpan(180, 345, 367)
    foot.addSpan(181, 345, 367)
    foot.addSpan(182, 345, 367)
    foot.addSpan(183, 345, 367)
    foot.addSpan(184, 345, 367)
    foot.addSpan(185, 345, 367)
    foot.addSpan(186, 345, 367)
    foot.addSpan(187, 345, 367)
    foot.addSpan(188, 345, 367)
    foot.addSpan(189, 345, 367)
    foot.addSpan(190, 345, 367)
    foot.addSpan(191, 345, 367)
    foot.addSpan(192, 345, 367)
    foot.addSpan(193, 345, 367)
    foot.addSpan(194, 345, 367)
    foot.addSpan(195, 345, 367)
    foot.addSpan(196, 345, 367)
    foot.addSpan(197, 345, 367)
    foot.addSpan(198, 345, 367)
    foot.addSpan(199, 345, 367)
    foot.addSpan(200, 345, 367)
    foot.addSpan(201, 345, 366)
    foot.addSpan(202, 345, 366)
    foot.addSpan(203, 345, 366)
    foot.addSpan(204, 345, 366)
    foot.addSpan(205, 345, 366)
    foot.addSpan(206, 345, 366)
    foot.addSpan(207, 345, 366)
    foot.addSpan(208, 345, 366)
    foot.addSpan(209, 345, 366)
    foot.addSpan(210, 344, 366)
    foot.addSpan(211, 344, 366)
    foot.addSpan(212, 344, 366)
    foot.addSpan(213, 344, 366)
    foot.addSpan(214, 345, 366)
    foot.addSpan(215, 345, 366)
    foot.addSpan(216, 345, 366)
    foot.addSpan(217, 345, 366)
    foot.addSpan(218, 345, 366)
    foot.addSpan(219, 345, 366)
    foot.addSpan(220, 345, 366)
    foot.addSpan(221, 345, 366)
    foot.addSpan(222, 345, 366)
    foot.addSpan(223, 345, 366)
    foot.addSpan(224, 345, 365)
    foot.addSpan(225, 345, 365)
    foot.addSpan(226, 345, 365)
    foot.addSpan(227, 345, 365)
    foot.addSpan(228, 345, 365)
    foot.addSpan(229, 345, 366)
    foot.addSpan(230, 345, 366)
    foot.addSpan(231, 345, 366)
    foot.addSpan(232, 345, 366)
    foot.addSpan(233, 345, 366)
    foot.addSpan(234, 345, 366)
    foot.addSpan(235, 345, 366)
    foot.addSpan(236, 345, 366)
    foot.addSpan(237, 345, 365)
    foot.addSpan(238, 345, 365)
    foot.addSpan(239, 345, 365)
    foot.addSpan(240, 345, 366)
    foot.addSpan(241, 345, 366)
    foot.addSpan(242, 345, 365)
    foot.addSpan(243, 345, 365)
    foot.addSpan(244, 345, 365)
    foot.addSpan(245, 345, 365)
    foot.addSpan(246, 345, 365)
    foot.addSpan(247, 345, 365)
    foot.addSpan(248, 345, 365)
    foot.addSpan(249, 345, 365)
    foot.addSpan(250, 338, 341)
    foot.addSpan(250, 345, 365)
    foot.addSpan(251, 337, 343)
    foot.addSpan(251, 345, 365)
    foot.addSpan(252, 336, 365)
    foot.addSpan(253, 336, 365)
    foot.addSpan(254, 337, 365)
    foot.addSpan(255, 337, 366)
    foot.addSpan(256, 337, 366)
    foot.addSpan(257, 337, 365)
    foot.addSpan(258, 337, 365)
    foot.addSpan(259, 338, 365)
    foot.addSpan(260, 338, 365)
    foot.addSpan(261, 339, 365)
    foot.addSpan(262, 339, 365)
    foot.addSpan(263, 341, 365)
    foot.addSpan(264, 346, 365)
    foot.addSpan(265, 346, 365)
    foot.addSpan(266, 346, 365)
    foot.addSpan(267, 346, 365)
    foot.addSpan(268, 346, 365)
    foot.addSpan(269, 346, 365)
    foot.addSpan(270, 346, 365)
    foot.addSpan(271, 346, 365)
    foot.addSpan(272, 346, 365)
    foot.addSpan(273, 346, 365)
    foot.addSpan(274, 346, 365)
    foot.addSpan(275, 346, 365)
    foot.addSpan(276, 346, 365)
    foot.addSpan(277, 346, 365)
    foot.addSpan(278, 346, 365)
    foot.addSpan(279, 346, 365)
    foot.addSpan(280, 346, 365)
    foot.addSpan(281, 346, 365)
    foot.addSpan(282, 346, 365)
    foot.addSpan(283, 346, 365)
    foot.addSpan(284, 345, 365)
    foot.addSpan(285, 342, 365)
    foot.addSpan(286, 342, 365)
    foot.addSpan(287, 341, 365)
    foot.addSpan(288, 341, 365)
    foot.addSpan(289, 340, 365)
    foot.addSpan(290, 340, 365)
    foot.addSpan(291, 339, 365)
    foot.addSpan(292, 335, 365)
    foot.addSpan(293, 334, 365)
    foot.addSpan(294, 333, 365)
    foot.addSpan(295, 333, 342)
    foot.addSpan(295, 346, 366)
    foot.addSpan(296, 333, 341)
    foot.addSpan(296, 346, 366)
    foot.addSpan(297, 333, 339)
    foot.addSpan(297, 346, 366)
    foot.addSpan(298, 333, 338)
    foot.addSpan(298, 346, 366)
    foot.addSpan(299, 346, 368)
    foot.addSpan(300, 346, 370)
    foot.addSpan(301, 346, 371)
    foot.addSpan(302, 346, 372)
    foot.addSpan(303, 346, 373)
    foot.addSpan(304, 346, 374)
    foot.addSpan(305, 346, 374)
    foot.addSpan(306, 346, 375)
    foot.addSpan(307, 346, 375)
    foot.addSpan(308, 346, 375)
    foot.addSpan(309, 345, 375)
    foot.addSpan(310, 345, 375)
    foot.addSpan(311, 345, 376)
    foot.addSpan(312, 344, 376)
    foot.addSpan(313, 344, 376)
    foot.addSpan(314, 344, 376)
    foot.addSpan(315, 344, 376)
    foot.addSpan(316, 343, 376)
    foot.addSpan(317, 343, 375)
    foot.addSpan(318, 342, 375)
    foot.addSpan(319, 341, 374)
    foot.addSpan(320, 341, 373)
    foot.addSpan(321, 341, 373)
    foot.addSpan(322, 341, 372)
    foot.addSpan(323, 341, 372)
    foot.addSpan(324, 341, 371)
    foot.addSpan(325, 341, 371)
    foot.addSpan(326, 341, 370)
    foot.addSpan(327, 342, 370)
    foot.addSpan(328, 342, 369)
    foot.addSpan(329, 342, 369)
    foot.addSpan(330, 342, 367)
    foot.addSpan(331, 343, 367)
    foot.addSpan(332, 343, 366)
    foot.addSpan(333, 343, 366)
    foot.addSpan(334, 342, 366)
    foot.addSpan(335, 342, 366)
    foot.addSpan(336, 342, 366)
    foot.addSpan(337, 342, 366)
    foot.addSpan(338, 342, 366)
    foot.addSpan(339, 343, 366)
    foot.addSpan(340, 344, 366)
    foot.addSpan(341, 345, 365)
    foot.addSpan(342, 346, 365)
    foot.addSpan(343, 346, 365)
    foot.addSpan(344, 346, 365)
    foot.normalize()
    return foot


if __name__ == '__main__':
    main()
    
