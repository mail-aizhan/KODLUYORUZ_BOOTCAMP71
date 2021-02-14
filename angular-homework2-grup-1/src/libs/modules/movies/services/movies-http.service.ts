import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { filter, map } from 'rxjs/operators';
import { IMovie } from '../models/movie-models';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MoviesHttpService {

  constructor(private http: HttpClient) { }

  getTop100Movies() {
    // TODO:
    // There are 250 movies in the dataset (top250movies.json)
    // This method should return an Observable that emits the first 100 movies (indexes from 1 to 100)
    
    //console.log("deneme")
    let a = this.http.get<[any]>('/assets/top250movies.json').pipe(
      map(arr => arr.slice(0,100))
    )
    a.subscribe(obj => console.log(obj))
    return a //...
  }

}
