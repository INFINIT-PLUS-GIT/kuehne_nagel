odoo.define('survey_theme.styles', function (require) {
    'use strict';


    $(document).ready(function(){
        if(!$(".o_survey_start").length){
            hide_background()
            $("#pagination_controls").addClass("show-flex")
        }else{
            $("#pagination_controls").removeClass("show-flex")
            $('button[value="start"').on("click",function(){
                hide_background()
                $("#pagination_controls").addClass("show-flex")
            })
            $(document).on("keydown",function(event){
                if (event.keyCode === 13) {
                    hide_background()
                    $("#pagination_controls").addClass("show-flex")
                }
            })
        }

        function show_background(){
            $("#wrapwrap").addClass("background-none")
            $(".o_survey_nav .container").show()
        }
        function hide_background(){
            $("#wrapwrap").addClass("background-none")
            $(".o_survey_nav .container").hide()
            $(".o_survey_form").addClass("without-margin-top")
            $(".o_survey_form_content").addClass("without-margin-top")
        }
    })
});