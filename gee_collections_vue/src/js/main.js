(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    jQuery(document).on('ready',function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 768) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').on('blur');
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).on('resize',toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).on('scroll',function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').on('click',function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
    
    
    // Header slider
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.header-slider').slick({
                autoplay: true,
                dots: true,
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1
            });
        });
    });
    
    // Product Slider 4 Column
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.product-slider-4').slick({
                autoplay: true,
                infinite: true,
                dots: false,
                slidesToShow: 4,
                slidesToScroll: 1,
                responsive: [
                    {
                        breakpoint: 1200,
                        settings: {
                            slidesToShow: 4,
                        }
                    },
                    {
                        breakpoint: 992,
                        settings: {
                            slidesToShow: 3,
                        }
                    },
                    {
                        breakpoint: 768,
                        settings: {
                            slidesToShow: 2,
                        }
                    },
                    {
                        breakpoint: 576,
                        settings: {
                            slidesToShow: 1,
                        }
                    },
                ]
            });
        });
    });
    
    
    // Product Slider 3 Column
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.product-slider-3').slick({
                autoplay: true,
                infinite: true,
                dots: false,
                slidesToShow: 3,
                slidesToScroll: 1,
                responsive: [
                    {
                        breakpoint: 992,
                        settings: {
                            slidesToShow: 3,
                        }
                    },
                    {
                        breakpoint: 768,
                        settings: {
                            slidesToShow: 2,
                        }
                    },
                    {
                        breakpoint: 576,
                        settings: {
                            slidesToShow: 1,
                        }
                    },
                ]
            });
        });
    });
    
    
    // Product Detail Slider
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.product-slider-single').slick({
                infinite: true,
                autoplay: true,
                dots: false,
                fade: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                asNavFor: '.product-slider-single-nav'
            });
        });
    });
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.product-slider-single-nav').slick({
                slidesToShow: 3,
                slidesToScroll: 1,
                dots: false,
                centerMode: true,
                focusOnSelect: true,
                asNavFor: '.product-slider-single'
            });
        });
    });
    
    
    // Brand Slider
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.brand-slider').slick({
                speed: 5000,
                autoplay: true,
                autoplaySpeed: 0,
                cssEase: 'linear',
                slidesToShow: 5,
                slidesToScroll: 1,
                infinite: true,
                swipeToSlide: true,
                centerMode: true,
                focusOnSelect: false,
                arrows: false,
                dots: false,
                responsive: [
                    {
                        breakpoint: 992,
                        settings: {
                            slidesToShow: 4,
                        }
                    },
                    {
                        breakpoint: 768,
                        settings: {
                            slidesToShow: 3,
                        }
                    },
                    {
                        breakpoint: 576,
                        settings: {
                            slidesToShow: 2,
                        }
                    },
                    {
                        breakpoint: 300,
                        settings: {
                            slidesToShow: 1,
                        }
                    }
                ]
            });
        });
    });
    
    // Review slider
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.review-slider').slick({
                autoplay: true,
                dots: false,
                infinite: true,
                slidesToShow: 2,
                slidesToScroll: 1,
                responsive: [
                    {
                        breakpoint: 768,
                        settings: {
                            slidesToShow: 1,
                        }
                    }
                ]
            });
        });
    });
    
    
    // Widget slider
    jQuery(function($) {
        jQuery(document).on('ready',function(){
            $('.sidebar-slider').slick({
                autoplay: true,
                dots: false,
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1
            });
        });
    });    
    
    // Quantity
    $('.qty button').on('click', function () {
        var $button = $(this);
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find('input').val(newVal);
    });

    
    // Shipping address show hide
    $('.checkout #shipto').on('change',function () {
        if($(this).is(':checked')) {
            $('.checkout .shipping-address').slideDown();
        } else {
            $('.checkout .shipping-address').slideUp();
        }
    });
    
    
    // Payment methods show hide
    $('.checkout .payment-method .custom-control-input').on('change',function () {
        if ($(this).prop('checked')) {
            var checkbox_id = $(this).attr('id');
            $('.checkout .payment-method .payment-content').slideUp();
            $('#' + checkbox_id + '-show').slideDown();
        }
    });
})(jQuery);

