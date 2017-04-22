angular.module('positions', [])
.controller('getPositions', function($scope, $http) {
    $http.get('http://192.168.0.194:5000/position/4').
        then(function(response) {
            $scope.positions = response.data;
        });
});