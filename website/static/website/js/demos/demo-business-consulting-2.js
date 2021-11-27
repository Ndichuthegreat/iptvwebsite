/*
Name: 			Business Consulting 2
Written by: 	iptvintel Themes - iptvintel
Theme Version:	8.3.0
*/

(function($) {

    'use strict';

    // Accordion
    $("[data-parent='#accordionServices']").on("click", function() {
        var trigger = $(this);
        $("#accordionServices .collapse.show").each(function() {
            if (trigger.attr("href") != ("#" + $(this).attr("id"))) {
                $(this).removeClass("show");
            }
        });
    });

}).apply(this, [jQuery]);