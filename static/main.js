
(function () {

  'use strict';

  angular.module('BeerListerApp', [])

  .controller('BeerListerController', ['$scope', '$log', '$http', function($scope, $log, $http) {
    $scope.getResults = function() {
      $log.log("test");
    };
  }

  ]);

}());