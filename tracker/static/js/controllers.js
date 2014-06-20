'use strict';

var ttControllers = angular.module('ttControllers',[]);

ttControllers.controller('RegisterCtrl',['$scope', '$http', 
    function($scope, $http){
        $scope.user = {}
        
        $scope.submitForm=function(){
            $http(
                {
                    method: "POST",
                    url :'http://localhost:5000/api/register',
                    data:JSON.stringify($scope.user),
                    headers: {'Content-Type': 'application/json'}
                }
            ).
            success(function(data, status, headers, config){
                
            }).
            error(function(data, status, headers, config){
                console.log(status);
            });
        }

    }]);
