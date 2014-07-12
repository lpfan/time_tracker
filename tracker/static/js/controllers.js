'use strict';

var ttControllers = angular.module('ttControllers',['LocalStorageModule']);

ttControllers.controller('RegisterCtrl',['$scope', '$http', 
    function($scope, $http){
        $scope.user = {}
        
        $scope.submitForm=function(form){
            $http(
                {
                    method: "POST",
                    url :'http://localhost:5000/api/register',
                    data:JSON.stringify($scope.user),
                    headers: {'Content-Type': 'application/json'}
                }
            ).
            success(function(data, status, headers, config){
                if (data.status === "unsuccess"){
                    $scope.usernameErrorMsg = data.reason;
                }
            });

        }
    }]);

ttControllers.controller('MainpageCtrl', ['$scope', 
    function($scope){
        
    }
])

ttControllers.controller('SignInCtrl', ['$scope', '$http', '$window',  
        function($scope, $http, $window){
            $scope.user = {};
            $scope.submitForm = function(form){
                $http(
                    {
                        method: "POST",
                        url: '/api/signin',
                        data: JSON.stringify($scope.user),
                        headers: {'Content-Type': 'application/json'}
                    }
                ).
                success(function(data, status, headers, config){
                    if (data.status === "unsuccess"){
                        console.log('error');
                        return;
                    }
                    $http.defaults.headers.common['Authentication'] = 'Base ' + data.token;
                    $window.location = '/user_dashboard';
                });
            }
        }]);

ttControllers.controller('DashboardCtrl', ['$scope', function($scope){

}]);

ttControllers.controller('TimeMgmtCtrl', ['$scope', '$http', '$timeout', 'localStorageService',
        function($scope, $http, $timeout, localStorageService){
            
            var taskToTrack = {
                'start_time':0,
                'end_time':0,
                'date':''
            }

            
            $scope.isDisabled = false;
            $scope.task = {};
            $scope.usefull_time = 0;
            $scope.useless_time = 0;
            var tickInterval = 1000;

            $scope.usefull_tick = function(){
                $scope.usefull_time += 1;
                $scope.usefull_timer = $timeout($scope.usefull_tick, tickInterval);
            }

            $scope.useless_tick = function(){
                $scope.useless_time += 1;
                $scope.useless_timer = $timeout($scope.useless_tick, tickInterval);
            }

            $scope.init = function(){
                //console.log('init');
                var c_date = new Date();
                var s_date = new Date().setHours(10,0,0);
                var seconds = (c_date - s_date)/1000;
                console.log(seconds);
                /*
                 *
                 * here should be initialization-call to API
                 *
                 */
                if (seconds > 0){
                    $scope.useless_time = seconds;
                    var timer = $timeout($scope.useless_tick, tickInterval);
                } else {
                    $scope.useless_time = "У вас усе ще попереду";
                }
            }

            $scope.startTimeTracking = function(form){
                var start_time = new Date().getTime()/1000;
                $scope.isDisabled = true;
                $scope.task.start_time = start_time;
                $http({
                    method: 'POST',
                    url: '/api/sync/start_task',
                    data: JSON.stringify($scope.task),
                    headers: {'Content-Type': 'application/json'}
                }).
                success(function(data, status, headers, config){
                    $timeout.cancel($scope.useless_timer);
                    var timer = $timeout($scope.usefull_tick, tickInterval);
                });
                return false;
            }

            $scope.stopTimeTracking = function(){
                var time = new Date();
                $scope.task.end_time = time.getTime() / 1000;
                $timeout.cancel($scope.usefull_timer);
                var timer = $timeout($scope.useless_tick, tickInterval);
                return false;
            }
        }
    ])
