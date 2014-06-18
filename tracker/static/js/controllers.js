'use strict';

var ttControllers = angular.module('ttControllers',[]);

ttControllers.controller('RegisterCtrl',['$scope', '$http', 
    function($scope, $http){
        console.log('register controller')
        
        $scope.formData = {}
        
        $scope.submitForm=function(){
            $scope.usernameRequired = '';
            $scope.emailRequired = '';

            if (!$scope.formData.username){
                $scope.usernameRequired = 'username то потрібний';
                return;
            }
            
            if (!$scope.formData.email){
                $scope.emailRequired = 'email то потрібний';
                return;
            }



            console.log($scope.formData);
        }

    }]);
