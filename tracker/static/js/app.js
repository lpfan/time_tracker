'use strict';

var ttApp = angular.module('ttApp', [
    'ngRoute',
    'ttControllers',
    'ttDirectivies'
]);

ttApp.config(['$routeProvider',
        function($routeProvider){
            $routeProvider.
                when('/register', {
                    templateUrl: '../templates/partials/register.html',
                    controller: 'RegisterCtrl'
                }).
                when('/signin', {
                    templateUrl:'../templates/partials/sign_in.html',
                    controller: 'SignInCtrl'
                }).
                when('/', {
                    templateUrl: '../templates/partials/main_page.html',
                    controller: 'MainpageCtrl'
                })
        }]);
