//
//  main.swift
//  KeyboardCrawler
//
//  Created by Do Yi Lee on 2022/02/26.
//

import Foundation
import SwiftSoup

let url = "https://www.daangn.com/search/기계식%20키보드"

enum CrawerError: Error {
    case addressInvalid
}

class Crawler {
    
    // 1. url바꾸기
    private func makeURL(url address: String) throws -> URL {
        guard let url = URL(string: address) else {
            print("url오류")
            throw CrawerError.addressInvalid
        }
        return url
    }
    
    //2. html로 바꾸고 SwiftSoup로 파싱하기
}
