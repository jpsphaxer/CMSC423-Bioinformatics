(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[4048],{fMoB:function(e,t,s){"use strict"
s.r(t)
var n=s("HGxv")
var i=s("ouhR")
var o=s.n(i)
s("w4it")
const r=Object(n["useScope"])("quizzes.quiz_submission")
o()(document).ready(()=>{o()("#questions.assessment_results .question").hover((function(){o()(this).addClass("hover")}),(function(){o()(this).removeClass("hover")}))
o()(".quiz_response_text img").each((function(){o()(this).css({borderColor:"#f44",borderStyle:"solid",borderWidth:"2px",padding:2}).attr("title",r.t("titles.this_is_an_image","This is an image, not text, and could have changed since the student submitted"))}))
o()(".quiz_response_text iframe").each((function(){o()(this).css({borderColor:"#f44",borderStyle:"solid",borderWidth:"2px",padding:2}).attr("title",r.t("titles.this_is_an_external_frame","This is an external frame, not text, and could have changed since the student submitted"))}))
const e=o()("nothing")
o()(".quiz_response_text").find("object,embed").each((function(){return e.add(o()(this).parents("object,embed:first"))}))
return e.each((function(){const e=o()("<span/>").css("display","inline-block")
e.before(o()(this))
e.append(o()(this))
return e.css({borderColor:"#f44",borderStyle:"solid",borderWidth:"2px",padding:2}).attr("title",r.t("titles.this_is_an_external_element","This is an external element, not text, and could have changed since the student submitted"))}))})},w4it:function(e,t,s){"use strict"
var n=s("ouhR")
var i=s.n(n)
i()(".question select").bind("mousewheel",e=>e.preventDefault())}}])

//# sourceMappingURL=quiz_submission-c-4710e53795.js.map